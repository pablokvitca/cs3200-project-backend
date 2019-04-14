import connexion
import six

from swagger_server.models.student import Student  # noqa: E501
from swagger_server import util

from swagger_server import encoder

from sqlalchemy import types
from sqlalchemy import exc

from flask import make_response


def logged_in_student_data(tries=0):
    def retry():
        if tries < 5:
            return logged_in_student_data(tries + 1)
        else:
            return "INTERNAL SERVER ERROR", 500

    try:
        session_cookie = connexion.request.cookies.get("session")
        session_NUID = connexion.JWT_verify(session_cookie)
        select_string = "SELECT * FROM student WHERE nuid = {}".format(session_NUID)
        db_conn = connexion.DB(connexion.DB_ENG)
        result = db_conn.execute(select_string)
        db_conn.close()
        res = []
        for r in result.fetchall():
            res.append({
                "nuid": r["nuid"],
                "email": r["email"],
                "name": r["name"]
            })
        if len(r) > 0:
            return res, 200
        else:
            return "User not logged in.", 400
    except:
        return retry()


def create_student(body):  # noqa: E501
    """Create student

    This can only be done by the logged in student. # noqa: E501

    :param body: Created student object
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Student.from_dict(connexion.request.get_json())  # noqa: E501
        insert_string = """
            INSERT INTO student (
                name,
                email,
                NUID,
                pass)
            VALUES (
                "{0}",
                "{1}",
                {2},
                "{3}");
            """.format(body.name, body.email, body.nuid, body.password)
        try:
            db_conn = connexion.DB(connexion.DB_ENG)
            db_conn.execute(insert_string)
            db_conn.close()
            return "Accepted", 201
        except exc.IntegrityError:
            return "Already Exists", 202
    return "Bad Request", 400


def delete_student(nuid):  # noqa: E501
    """Delete student

    This can only be done by the logged in student. # noqa: E501

    :param nuid: The nuid that needs to be deleted
    :type nuid: str

    :rtype: None
    """
    delete_string = """
        DELETE FROM student
        WHERE nuid = "{}"
        """.format(nuid)
    try:
        db_conn = connexion.DB(connexion.DB_ENG)
        db_conn.execute(delete_string)
        db_conn.close()
        return "Deleted", 204
    except exc.IntegrityError:
        return "Could not delete object", 403


def get_student_by_nuid(nuid):  # noqa: E501
    """Get student by nuid

     # noqa: E501

    :param nuid: The name that needs to be fetched. Use student1 for testing.
    :type nuid: int

    :rtype: Student
    """
    select_string = """
        SELECT
            name,
            email,
            nuid
        FROM
            student
        WHERE
            nuid = {}
        """.format(nuid)
    try:
        db_conn = connexion.DB(connexion.DB_ENG)
        result = db_conn.execute(select_string)
        db_conn.close()
        for row in result:
            res = {
                'name': row["name"],
                'nuid': row["nuid"],
                'email': row["email"]
            }
            res = Student.from_dict(res)
            return res, 200
        return "Object not found", 404
    except exc.IntegrityError:
        return "Internal Server Error", 500


def login_student(nuid, password):  # noqa: E501
    """Logs student into the system

     # noqa: E501

    :param nuid: The nuid for login
    :type nuid: str
    :param password: The password for login in clear text
    :type password: str

    :rtype: str
    """
    select_string = """
        SELECT
            name,
            email,
            nuid
        FROM
            student
        WHERE
            nuid = {0}
            AND
            pass = "{1}";
        """.format(nuid, password)
    db_conn = connexion.DB(connexion.DB_ENG)
    result = db_conn.execute(select_string)
    db_conn.close()

    for row in result:
        resp = make_response("Student is now logged in", 200)
        session = connexion.JWT_generate_token(nuid)
        resp.set_cookie("session", session)
        return resp
    else:
        resp = make_response(
            "Wrong User/Password Combination. Please try again.", 403)
        session = 'logged_out'
        resp.set_cookie("session", session)
        return resp


def logout_student():  # noqa: E501
    """Logs out current logged in student session

     # noqa: E501


    :rtype: None
    """
    resp = make_response("Student logged out", 200)
    session = 'logged_out'
    resp.set_cookie("session", session)
    return resp


def update_student(nuid, body):  # noqa: E501
    """Updated student

    This can only be done by the logged in student. # noqa: E501

    :param nuid: nuid that need to be updated
    :type nuid: int
    :param body: Updated student object
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Student.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
