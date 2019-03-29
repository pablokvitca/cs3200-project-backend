import connexion
import six

from swagger_server.models.department import Department  # noqa: E501
from swagger_server import util


def add_department(body):  # noqa: E501
    """Add a department to the classdeck

     # noqa: E501

    :param body: Department object that needs to be added to the system
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Department.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_department(department_short_code):  # noqa: E501
    """Deletes a department

     # noqa: E501

    :param department_short_code: Department short code to delete
    :type department_short_code: str

    :rtype: None
    """
    return 'do some magic!'


def get_department_by_short_code(department_short_code):  # noqa: E501
    """Find department by short code

    Returns a single department # noqa: E501

    :param department_short_code: short code of department to return
    :type department_short_code: str

    :rtype: Department
    """
    return 'do some magic!'


def update_department(body):  # noqa: E501
    """Update an existing department

     # noqa: E501

    :param body: Department object that needs to be updated in the system
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Department.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
