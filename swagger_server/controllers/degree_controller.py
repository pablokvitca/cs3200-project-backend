import connexion
import six

from swagger_server.models.degree import Degree  # noqa: E501
from swagger_server import util


def add_degree(body):  # noqa: E501
    """Add a degree to the classdeck

     # noqa: E501

    :param body: Degree object that needs to be added to the system
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Degree.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def degree_list_prereqs(degree_id):  # noqa: E501
    """List the prereqs for a given degree

     # noqa: E501

    :param degree_id: Degree id to delete
    :type degree_id: int

    :rtype: None
    """
    return 'do some magic!'


def delete_degree(degree_id):  # noqa: E501
    """Deletes a degree

     # noqa: E501

    :param degree_id: Degree id to delete
    :type degree_id: int

    :rtype: None
    """
    return 'do some magic!'


def get_degree_by_id(degree_id):  # noqa: E501
    """Find degree by ID

    Returns a single degree # noqa: E501

    :param degree_id: ID of degree to return
    :type degree_id: int

    :rtype: Degree
    """
    return 'do some magic!'


def list_degrees():  # noqa: E501
    """List all degrees

     # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def list_degrees_by_college(college_id):  # noqa: E501
    """List all degrees in the given college

     # noqa: E501

    :param college_id: ID of college related to the degrees to return
    :type college_id: int

    :rtype: None
    """
    return 'do some magic!'


def update_degree(body):  # noqa: E501
    """Update an existing degree

     # noqa: E501

    :param body: Degree object that needs to be updated in the system
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Degree.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
