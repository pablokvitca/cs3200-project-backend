import connexion
import six

from swagger_server.models.student import Student  # noqa: E501
from swagger_server import util

from swagger_server import encoder

from sqlalchemy import types
from sqlalchemy import exc

from flask import make_response


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
            connexion.DB.execute(insert_string)
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
        connexion.DB.execute(delete_string)
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
        result = connexion.DB.execute(select_string)
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
    result_user = connexion.DB.execute(select_string)

    for row in result_user:
        resp = make_response("Student logged in", 200)
        session = '{{ nuid: {0}, jwt: {1} }}'.format(nuid, "secret")
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
