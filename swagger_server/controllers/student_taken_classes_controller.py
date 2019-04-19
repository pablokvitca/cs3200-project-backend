import connexion
import six

from swagger_server.models.student_taken_classes import StudentTakenClasses  # noqa: E501
from swagger_server import util

from swagger_server import encoder

from sqlalchemy import types
from sqlalchemy import exc

from flask import make_response


def add_student_taken_classes(body):  # noqa: E501
    """Add a student_taken_classes to the classdeck

     # noqa: E501

    :param body: StudentTakenClasses object that needs to be added to the system
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = StudentTakenClasses.from_dict(connexion.request.get_json())  # noqa: E501
        insert_string = """
            INSERT IGNORE INTO classes_taken (
                nuid,
                class_dept,
                class_number,
                current,
                transferred)
            VALUES ({0}, "{1}", {2}, {3}, {4});
            """.format(body.nuid, body.class_dept, body.class_number, body.current, body.transferred)
        try:
            session_cookie = connexion.request.cookies.get("session")
            session_NUID = connexion.JWT_verify(session_cookie)
            if session_NUID == str(body.nuid).zfill(9):
                db_conn = connexion.DB(connexion.DB_ENG)
                result = db_conn.execute(insert_string)
                db_conn.close()
                return "Accepted", 201
            else:
                return "Forbidden", 403
        except exc.IntegrityError as err:
            return "Could not add classes taken", 406
        except KeyError:
            return "Forbidden", 403
    return "Bad Request", 400


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
    delete_string = """
            DELETE FROM classes_taken 
            WHERE nuid = {0} 
              AND class_dept = '{1}'
              AND class_number = {2};
            """.format(nuid, class_dept, class_number)
    try:
        session_cookie = connexion.request.cookies.get("session")
        session_NUID = connexion.JWT_verify(session_cookie)
        if session_NUID == str(nuid).zfill(9):
            db_conn = connexion.DB(connexion.DB_ENG)
            result = db_conn.execute(delete_string)
            db_conn.close()
            return "Accepted", 201
        else:
            return "Forbidden", 403
    except exc.IntegrityError:
        return "Could delete classes taken", 406
    except KeyError:
        return "Forbidden", 403


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
