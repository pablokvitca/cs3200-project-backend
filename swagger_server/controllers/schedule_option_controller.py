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
                result = connexion.DB.execute(insert_string)
                return ["Accepted", result.lastrowid], 201
            else:
                return "Forbidden", 403
        except exc.IntegrityError as err:
            return "Could not add pursued degree", 406
        except KeyError:
            return "Forbidden", 403
    return "Bad Request", 400


def delete_schedule_option(schedule_option_id, tries=0):  # noqa: E501
    """Deletes a schedule_option

     # noqa: E501

    :param schedule_option_id: ScheduleOption id to delete
    :type schedule_option_id: int

    :rtype: None
    """

    def retry():
        if tries < 5:
            return delete_schedule_option(schedule_option_id, tries + 1)
        else:
            return "I'm Done", 420

    delete_string = "DELETE FROM schedule_option WHERE schedule_option_id = {0};".format(schedule_option_id)
    try:
        session_cookie = connexion.request.cookies.get("session")
        session_NUID = connexion.JWT_verify(session_cookie)
        connexion.DB.execute(delete_string)
        return "Accepted", 201
    except exc.IntegrityError:
        return "Could not add pursued degree", 406
    except exc.InterfaceError:
        retry()
    except exc.OperationalError:
        retry()
    except exc.InternalError:
        retry()
    except KeyError:
        return "Forbidden", 403


def get_schedule_option_by_nuid(nuid):  # noqa: E501
    """List schedule_option by NUID

    Returns the schedule_options related to the given NUID # noqa: E501

    :param nuid: nuid of the user related to the schedule_option to return
    :type nuid: int

    :rtype: None
    """
    select_string = """
            SELECT
                opt.schedule_option_id, 
                opt.title, 
                opt.semester_id, 
                sec.crn, 
                sec.class_dept, 
                sec.class_number, 
                sec.professor,
                mt.start_time,
                mt.end_time,
                mt.meeting_days
            FROM schedule_option AS opt
            LEFT OUTER JOIN schedule_option_section AS opt_s ON opt.schedule_option_id = opt_s.schedule_option_id
            LEFT OUTER JOIN section AS sec ON opt_s.section_crn = sec.crn
            LEFT OUTER JOIN meeting_times AS mt ON sec.crn = mt.crn
            WHERE nuid = {};
            """.format(nuid)
    try:
        session_cookie = connexion.request.cookies.get("session")
        session_NUID = connexion.JWT_verify(session_cookie)
        if session_NUID == str(nuid).zfill(9):
            print(connexion.DB.default_isolation_level)
            result = connexion.DB.execute(select_string)
            res = []
            opt = {
                "schedule_option_id": -1,
                "nuid": -1,
                "title": -1,
                "semester_id": -1,
                "sections": []
            }
            for schedule_option_id, title, semester_id, crn, class_dept, \
                    class_number, professor, start_time, end_time, meeting_days in result.fetchall():
                if opt["schedule_option_id"] == schedule_option_id:
                    opt["sections"].append({
                        "class_dept": class_dept,
                        "class_number": class_number,
                        "professor": professor,
                        "crn": crn
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
                        opt["sections"].append({
                            "class_dept": class_dept,
                            "class_number": class_number,
                            "professor": professor,
                            "crn": crn
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
