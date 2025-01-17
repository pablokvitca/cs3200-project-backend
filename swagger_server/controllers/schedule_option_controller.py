import connexion
import six

from swagger_server.models.schedule_option import ScheduleOption  # noqa: E501
from swagger_server import util

from sqlalchemy import exc


def add_schedule_option(body):  # noqa: E501
    """Add a schedule_option to the classdeck

     # noqa: E501

    :param body: ScheduleOption object that needs to be added to the system
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        json = connexion.request.get_json()
        body = ScheduleOption.from_dict(json)  # noqa: E501
        insert_string = """
                    INSERT INTO schedule_option (nuid, title, semester_id)
                    VALUES ({0}, '{1}', {2});
                    """.format(json["nuid"], json["title"], json["semester"])
        try:
            session_cookie = connexion.request.cookies.get("session")
            session_NUID = connexion.JWT_verify(session_cookie)
            if session_NUID == str(body.nuid).zfill(9):
                db_conn = connexion.DB(connexion.DB_ENG)
                trans = db_conn.begin()
                result = db_conn.execute(insert_string)
                trans.commit()
                db_conn.close()
                return ["Accepted", result.lastrowid], 201
            else:
                return "Forbidden", 403
        except exc.IntegrityError as err:
            return "Could not add pursued degree", 406
        except KeyError:
            return "Forbidden", 403
    return "Bad Request", 400


def delete_schedule_option(schedule_option_id):  # noqa: E501
    """Deletes a schedule_option

     # noqa: E501

    :param schedule_option_id: ScheduleOption id to delete
    :type schedule_option_id: int

    :rtype: None
    """
    delete_string = "DELETE FROM schedule_option WHERE schedule_option_id = {0};".format(schedule_option_id)
    try:
        session_cookie = connexion.request.cookies.get("session")
        session_NUID = connexion.JWT_verify(session_cookie)
        db_conn = connexion.DB(connexion.DB_ENG)
        result = db_conn.execute(delete_string)
        db_conn.close()
        return "Accepted", 201
    except exc.IntegrityError:
        return "Could not delete schedule option", 406
    except KeyError:
        return "Forbidden", 403


def duplicate_schedule_option(sch_opt_id):
    try:
        session_cookie = connexion.request.cookies.get("session")
        session_NUID = connexion.JWT_verify(session_cookie)
        db_conn = connexion.DB_ENG.raw_connection()
        cursor = db_conn.cursor()
        cursor.callproc("duplicate_schedule_option", [sch_opt_id])
        db_conn.commit()
        cursor.close()
        db_conn.close()
        return "Accepted", 200
    except exc.IntegrityError:
        return "Server error", 500
    except KeyError:
        return "Forbidden", 403


def update_schedule_option():
    if connexion.request.is_json:
        body: ScheduleOption = ScheduleOption.from_dict(connexion.request.get_json())  # noqa: E501
        update_string = """
            UPDATE schedule_option
            SET title  = "{1}"
            WHERE schedule_option_id = {0};
            """.format(body.schedule_id, body.title)
        try:
            session_cookie = connexion.request.cookies.get("session")
            session_NUID = connexion.JWT_verify(session_cookie)
            db_conn = connexion.DB(connexion.DB_ENG)
            db_conn.execute(update_string)
            db_conn.close()
            return "Accepted", 201
        except exc.IntegrityError:
            return "Already Exists", 202
        except KeyError:
            return "Forbidden", 403
    return "Bad Request", 400


def get_schedule_option_by_nuid(nuid):  # noqa: E501
    """List schedule_option by NUID

    Returns the schedule_options related to the given NUID # noqa: E501

    :param nuid: nuid of the user related to the schedule_option to return
    :type nuid: int

    :rtype: None
    """
    select_string = """
            SELECT
                DISTINCT
                opt.schedule_option_id, 
                opt.title, 
                opt.semester_id, 
                sec.crn, 
                sec.class_dept, 
                sec.class_number, 
                sec.professor,
                mt.start_time,
                mt.end_time,
                mt.meeting_days,
                cls.name,
                cls.description,
                satisfies_degree_requirement({0}, cls.class_dept, cls.class_number) AS part_of_degree
            FROM schedule_option AS opt
            LEFT OUTER JOIN schedule_option_section AS opt_s ON opt.schedule_option_id = opt_s.schedule_option_id
            LEFT OUTER JOIN section AS sec ON opt_s.section_crn = sec.crn
            LEFT OUTER JOIN meeting_times AS mt ON sec.crn = mt.crn
            LEFT OUTER JOIN class AS cls ON (sec.class_dept = cls.class_dept AND sec.class_number = cls.class_number)
            WHERE nuid = {0};
            """.format(nuid)
    try:
        session_cookie = connexion.request.cookies.get("session")
        session_NUID = connexion.JWT_verify(session_cookie)
        if session_NUID == str(nuid).zfill(9):
            db_conn = connexion.DB(connexion.DB_ENG)
            result = db_conn.execute(select_string)
            db_conn.close()
            res = []
            opt = {
                "schedule_option_id": -1,
                "nuid": -1,
                "title": -1,
                "semester_id": -1,
                "sections": []
            }
            for schedule_option_id, title, semester_id, crn, class_dept, \
                class_number, professor, start_time, end_time, meeting_days, \
                cname, cdesc, part_of_degree in result.fetchall():
                if opt["schedule_option_id"] == schedule_option_id:
                    mapped_crns = list(map(lambda s: s["crn"], opt["sections"]))
                    if crn not in mapped_crns:
                        opt["sections"].append({
                            "class_dept": class_dept,
                            "class_number": class_number,
                            "professor": professor,
                            "crn": crn,
                            "cname": cname,
                            "cdesc": cdesc,
                            "part_of_degree": part_of_degree
                        })
                else:
                    if opt["schedule_option_id"] != -1:
                        res.append(opt)
                    opt = {
                        "schedule_option_id": schedule_option_id,
                        "nuid": nuid,
                        "title": title,
                        "semester_id": semester_id,
                        "sections": []
                    }
                    if crn is not None:
                        mapped_crns = list(map(lambda s: s["crn"], opt["sections"]))
                        if crn not in mapped_crns:
                            opt["sections"].append({
                                "class_dept": class_dept,
                                "class_number": class_number,
                                "professor": professor,
                                "crn": crn,
                                "cname": cname,
                                "cdesc": cdesc,
                                "part_of_degree": part_of_degree
                            })
            if opt["schedule_option_id"] != -1:
                res.append(opt)
            return res, 201
        else:
            return "Forbidden", 403
    except exc.IntegrityError as err:
        return "Could not add pursued degree", 406
    except KeyError:
        return "Forbidden", 403
