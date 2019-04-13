import connexion
import six

from swagger_server.models.schedule_option_section import ScheduleOptionSection  # noqa: E501
from swagger_server import util

from sqlalchemy import exc


def add_schedule_option_section(body, tries=0):  # noqa: E501
    """Add a schedule_option_section to the classdeck

     # noqa: E501

    :param body: ScheduleOptionSection object that needs to be added to the system
    :type body: dict | bytes

    :rtype: None
    """
    def retry():
        if tries < 5:
            return add_schedule_option_section(body, tries + 1)
        else:
            return []

    if connexion.request.is_json:
        body = ScheduleOptionSection.from_dict(connexion.request.get_json())  # noqa: E501
        insert_string = """
                    INSERT INTO schedule_option_section (schedule_option_id, section_crn)
                        VALUES ({0}, {1});
                    """.format(body.schedule_id, body.crn)
        try:
            session_cookie = connexion.request.cookies.get("session")
            session_NUID = connexion.JWT_verify(session_cookie)
            result = connexion.DB.execute(insert_string)
            return ["Accepted", result.lastrowid], 201
        except exc.IntegrityError as err:
            return "Could add section for schedule_option", 406
        except KeyError:
            return "Forbidden", 403
        except:
            return retry()
    return "Bad Request", 400


def delete_schedule_option_section(schedule_id, crn, tries=0):  # noqa: E501
    """Deletes a schedule_option_section

     # noqa: E501

    :param schedule_id: ID of the schedule related to the schedule_option_section to return
    :type schedule_id: int
    :param crn: crn of the section related to the schedule_option_section to return
    :type crn: int

    :rtype: None
    """
    def retry():
        if tries < 5:
            delete_schedule_option_section(schedule_id, crn, tries + 1)

    delete_string = "DELETE FROM schedule_option_section WHERE schedule_option_id = {0} AND section_crn = {1};"\
        .format(schedule_id, crn)
    try:
        session_cookie = connexion.request.cookies.get("session")
        session_NUID = connexion.JWT_verify(session_cookie)
        connexion.DB.execute(delete_string)
        return "Accepted", 201
    except exc.IntegrityError:
        return "Could not remove section", 202
    except exc.InterfaceError:
        retry()
    except exc.OperationalError:
        retry()
    except exc.InternalError:
        retry()
    except KeyError:
        return "Forbidden", 403