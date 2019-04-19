import connexion
import six

from swagger_server.models.student_taken_classes import StudentTakenClasses  # noqa: E501
from swagger_server import util


def add_student_taken_classes(body):  # noqa: E501
    """Add a student_taken_classes to the classdeck

     # noqa: E501

    :param body: StudentTakenClasses object that needs to be added to the system
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = StudentTakenClasses.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_student_taken_classes(nuid, class_dept, class_number):  # noqa: E501
    """Deletes a student_taken_classes

     # noqa: E501

    :param nuid: nuid of the student related to the student_taken_classes to return
    :type nuid: int
    :param class_dept: short code of the department of the class related to the student_taken_classes to return
    :type class_dept: str
    :param class_number: number of the class related to the student_taken_classes to return
    :type class_number: int

    :rtype: None
    """
    return 'do some magic!'


def get_student_taken_classes_by_nuid(nuid):  # noqa: E501
    """Find student_taken_classes by ID

    Returns a single student_taken_classes # noqa: E501

    :param nuid: nuid of the student related to the student_taken_classes to return
    :type nuid: int
    :param class_dept: short code of the department of the class related to the student_taken_classes to return
    :type class_dept: str
    :param class_number: number of the class related to the student_taken_classes to return
    :type class_number: int

    :rtype: StudentTakenClasses
    """
    select_string = """
            SELECT nuid, class_dept, class_number, transferred, current 
            FROM classes_taken
            WHERE
                nuid = {};
            """.format(nuid)
    try:
        session_cookie = connexion.request.cookies.get("session")
        session_NUID = connexion.JWT_verify(session_cookie)
        if session_NUID == str(nuid).zfill(9):
            db_conn = connexion.DB(connexion.DB_ENG)
            result = db_conn.execute(select_string)
            db_conn.close()
            res = []
            for nuid, class_dept, class_number, transferred, current in result.fetchall():
                r = StudentTakenClasses(nuid, class_dept, class_number, transferred, current)
                res.append(r)
            return res, 201
        else:
            return "Forbidden", 403
    except KeyError:
        return "Forbidden", 403
    except AttributeError:
        return "Forbidden", 403


def update_student_taken_classes(body):  # noqa: E501
    """Update an existing student_taken_classes

     # noqa: E501

    :param body: StudentTakenClasses object that needs to be updated in the system
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = StudentTakenClasses.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
