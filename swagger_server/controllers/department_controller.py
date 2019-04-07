import connexion
import six

from swagger_server.models.department import Department  # noqa: E501
from swagger_server import util


def get_department_by_short_code(department_short_code):  # noqa: E501
    """Find department by short code

    Returns a single department # noqa: E501

    :param department_short_code: short code of department to return
    :type department_short_code: str

    :rtype: Department
    """
    return 'do some magic!'


def list_department():  # noqa: E501
    """List all departments

     # noqa: E501


    :rtype: None
    """
    return 'do some magic!'
