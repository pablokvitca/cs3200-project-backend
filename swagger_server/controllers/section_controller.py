import connexion
import six

from swagger_server.models.section import Section  # noqa: E501
from swagger_server import util

from sqlalchemy import types
from sqlalchemy import exc
from pymysql import err


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
        result = connexion.DB.execute(select_string)
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


def list_sections():  # noqa: E501
    """Lists all sections

     # noqa: E501


    :rtype: None
    """
    select_string = """
                SELECT * FROM section
                """
    try:
        result = connexion.DB.execute(select_string)
        res = []
        for row in result:
            r = Section.from_dict(row)
            res.append({
                'CRN': row["CRN"],
                'class_dept': row["class_dept"],
                'class_number': row["class_number"],
                'professor': row["professor"],
                'capacity': row["capacity"],
                'registered': row["registered"]
            })
        return res, 200
    except exc.IntegrityError:
        return "Internal Server Error", 500


def list_sections_filtered(sch_opt_id):
    conn = connexion.DB_ENG.raw_connection()
    cursor = conn.cursor()

    result = []
    try:
        res = cursor.callproc("select_filtered_sections", [sch_opt_id])
        sec = {
            "crn": -1,
            "class_dept": -1,
            "class_number": -1,
            "professor": -1,
            "semester_id": -1,
            "cname": -1,
            "cdesc": -1,
            "meeting_times": []
        }

        for crn, class_dept, class_number, professor, semester_id, \
                start_time, end_time, meeting_days, cname, cdesc in cursor.fetchall():
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
                    "meeting_times": []
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
    finally:
        cursor.close()
        conn.close()
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