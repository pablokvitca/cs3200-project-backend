import connexion
import six

from swagger_server.models.semester import Semester  # noqa: E501
from swagger_server import util


def add_semester(body):  # noqa: E501
    """Add a semester to the classdeck

     # noqa: E501

    :param body: Semester object that needs to be added to the system
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Semester.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_semester(semester, year):  # noqa: E501
    """Deletes a semester

     # noqa: E501

    :param semester: semester to return
    :type semester: str
    :param year: year to return
    :type year: int

    :rtype: None
    """
    return 'do some magic!'


def get_semester_by_id(semester, year):  # noqa: E501
    """Find semester by ID

    Returns a single semester # noqa: E501

    :param semester: semester to return
    :type semester: str
    :param year: year to return
    :type year: int

    :rtype: Semester
    """
    return 'do some magic!'


def update_semester(body):  # noqa: E501
    """Update an existing semester

     # noqa: E501

    :param body: Semester object that needs to be updated in the system
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Semester.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
