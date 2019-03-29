import connexion
import six

from swagger_server.models.student import Student  # noqa: E501
from swagger_server import util


def create_student(body):  # noqa: E501
    """Create student

    This can only be done by the logged in student. # noqa: E501

    :param body: Created student object
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Student.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_student(nuid):  # noqa: E501
    """Delete student

    This can only be done by the logged in student. # noqa: E501

    :param nuid: The nuid that needs to be deleted
    :type nuid: str

    :rtype: None
    """
    return 'do some magic!'


def get_student_by_nuid(nuid):  # noqa: E501
    """Get student by nuid

     # noqa: E501

    :param nuid: The name that needs to be fetched. Use student1 for testing.
    :type nuid: int

    :rtype: Student
    """
    return 'do some magic!'


def login_student(nuid, password):  # noqa: E501
    """Logs student into the system

     # noqa: E501

    :param nuid: The nuid for login
    :type nuid: str
    :param password: The password for login in clear text
    :type password: str

    :rtype: str
    """
    return 'do some magic!'


def logout_student():  # noqa: E501
    """Logs out current logged in student session

     # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


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
