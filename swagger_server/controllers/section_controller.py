import connexion
import six

from swagger_server.models.section import Section  # noqa: E501
from swagger_server import util

from sqlalchemy import types
from sqlalchemy import exc
from pymysql import err
from swagger_server.controllers.class_prereq_group_controller import get_class_prereqs_db
from swagger_server.controllers.class_prereq_group_controller import Prereq
import re


def get_section_by_crn(crn):  # noqa: E501
    """Find section by

    Returns a single section # noqa: E501

    :param crn: CRN of section to return
    :type crn: int

    :rtype: Section
    """
    select_string = """
                        SELECT 
                            sec.crn,
                            sec.class_dept,
                            sec.class_number,
                            sec.professor,
                            sec.capacity,
                            sec.registered,
                            mt.start_time,
                            mt.end_time,
                            mt.meeting_days
                        FROM section AS sec
                        LEFT OUTER JOIN meeting_times AS mt ON sec.crn = mt.crn
                        WHERE sec.crn = "{}"
                        """.format(crn)
    try:
        db_conn = connexion.DB(connexion.DB_ENG)
        result = db_conn.execute(select_string)
        db_conn.close()
        res = []
        opt = {
                'crn': -1,
                'class_dept': -1,
                'class_number': -1,
                'professor': -1,
                'capacity': -1,
                'registered': -1,
                "meeting_times": []
            }
        for crn, class_dept, class_number, professor, capacity, \
                registered, start_time, end_time, meeting_days in result.fetchall():
            if opt["crn"] == crn:
                if not isinstance(meeting_days, type(None)):
                    opt["meeting_times"].append({
                        "start_time": str(start_time)[:-3],
                        "end_time": str(end_time)[:-3],
                        "meeting_days": mt_days_proc(meeting_days)
                    })
            else:
                if opt["crn"] != -1:
                    res.append(opt)
                opt = {
                    'crn': crn,
                    'class_dept': class_dept,
                    'class_number': class_number,
                    'professor': professor,
                    'capacity': capacity,
                    'registered': registered,
                    "meeting_times": []
                }
                if not isinstance(meeting_days, type(None)):
                    opt["meeting_times"].append({
                        "start_time": str(start_time)[:-3],
                        "end_time": str(end_time)[:-3],
                        "meeting_days": mt_days_proc(meeting_days)
                    })
        if opt["crn"] != -1:
            res.append(opt)
        if len(res) == 0:
            return "Object not found", 404
        return res[0], 200
    except exc.InternalError:
        return "Internal Server Error", 500


def list_sections_by_class(semester_id, class_department, class_number):
    select_string = """
                    SELECT * 
                    FROM section AS s
                    WHERE s.semester_id = {0}
                      AND s.class_dept = "{1}"
                      AND s.class_number = {2};
                    """.format(semester_id, class_department, class_number)
    try:
        db_conn = connexion.DB(connexion.DB_ENG)
        result = db_conn.execute(select_string)
        db_conn.close()
        res = []
        for row in result:
            r = Section.from_dict(row)
            res.append({
                'crn': row["crn"],
                'class_dept': row["class_dept"],
                'class_number': row["class_number"],
                'professor': row["professor"],
                'capacity': row["capacity"],
                'registered': row["registered"]
            })
        return res, 200
    except exc.IntegrityError:
        return "Internal Server Error", 500


def list_sections():  # noqa: E501
    """Lists all sections

     # noqa: E501


    :rtype: None
    """
    select_string = """
                SELECT * FROM section
                """
    try:
        db_conn = connexion.DB(connexion.DB_ENG)
        result = db_conn.execute(select_string)
        db_conn.close()
        res = []
        for row in result:
            r = Section.from_dict(row)
            res.append({
                'crn': row["crn"],
                'class_dept': row["class_dept"],
                'class_number': row["class_number"],
                'professor': row["professor"],
                'capacity': row["capacity"],
                'registered': row["registered"]
            })
        return res, 200
    except exc.IntegrityError:
        return "Internal Server Error", 500


def list_sections_filtered(sch_opt_id, search_query):
    conn = connexion.DB_ENG.raw_connection()
    cursor = conn.cursor()

    result = []
    try:
        search_query = re.sub(' ', '%', search_query)
        res = cursor.callproc("select_filtered_sections", [sch_opt_id, search_query])
        sec = {
            "crn": -1,
            "class_dept": -1,
            "class_number": -1,
            "professor": -1,
            "semester_id": -1,
            "cname": -1,
            "cdesc": -1,
            "meeting_times": [],
            "part_of_degree": -1
        }

        for crn, class_dept, class_number, \
            professor, semester_id, \
            start_time, end_time, meeting_days, \
            cname, cdesc, part_of_degree \
                in cursor.fetchall():
            if sec["crn"] == crn:
                if not isinstance(meeting_days, type(None)):
                    sec["meeting_times"].append({
                        "start_time": str(start_time)[:-3],
                        "end_time": str(end_time)[:-3],
                        "meeting_days": mt_days_proc(meeting_days),
                    })
            else:
                if sec["crn"] != -1:
                    result.append(sec)
                sec = {
                    "crn": crn,
                    "class_dept": class_dept,
                    "class_number": class_number,
                    "professor": professor,
                    "semester_id": semester_id,
                    "cname": cname,
                    "cdesc": cdesc,
                    "meeting_times": [],
                    "part_of_degree": part_of_degree
                }
                if not isinstance(meeting_days, type(None)):
                    sec["meeting_times"].append({
                        "start_time": str(start_time)[:-3],
                        "end_time": str(end_time)[:-3],
                        "meeting_days": mt_days_proc(meeting_days),
                    })
        if sec["crn"] != -1:
            result.append(sec)
    except err.InternalError as e:
        print("ERROR", e)
        return "Internal Server error", 500
    finally:
        cursor.close()
        conn.close()

        db_conn = connexion.DB(connexion.DB_ENG)
        select_string = """
                                SELECT 
                                    ct.class_dept,
                                    ct.class_number
                                FROM classes_taken AS ct
                                NATURAL JOIN schedule_option AS sch_opt
                                WHERE sch_opt.schedule_option_id = {};
                                """.format(sch_opt_id)
        result_classes_taken = db_conn.execute(select_string)
        db_conn.close()
        classes_taken = []
        for row in result_classes_taken:
            classes_taken.append({
                'class_dept': row["class_dept"],
                'class_number': row["class_number"]
            })

        def filter_meets_prerequisites(sec):
            prereqs: Prereq = get_class_prereqs_db(sec["class_dept"], sec["class_number"])
            return True if isinstance(prereqs, dict) else prereqs.meets_prereqs(classes_taken)

        result = list(filter(filter_meets_prerequisites, result))
        return result, 200


def mt_days_proc(mt):
    pos_to_day = ("M", "T", "W", "R", "F", "S", "U")
    res = ""
    pos = 0
    for b in mt:
        if b == 49:
            res += pos_to_day[pos]
        pos += 1
    return res


def restrictions_by_crn(crn):
    select_string = """
                    SELECT * FROM restriction
                    WHERE crn = {}
                    """.format(crn)
    try:
        db_conn = connexion.DB(connexion.DB_ENG)
        result = db_conn.execute(select_string)
        db_conn.close()
        res = []
        for row in result:
            res.append({
                'crn': row["crn"],
                'type': row[type]
            })
        return res, 200
    except exc.IntegrityError:
        return "Internal Server Error", 500