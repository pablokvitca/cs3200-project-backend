import connexion
import six

from swagger_server.models.college import College  # noqa: E501
from swagger_server import util


def add_college(body):  # noqa: E501
    """Add a college to the classdeck

     # noqa: E501

    :param body: College object that needs to be added to the system
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = College.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_college(college_id):  # noqa: E501
    """Deletes a college

     # noqa: E501

    :param college_id: College  id to delete
    :type college_id: int

    :rtype: None
    """
    return 'do some magic!'


def get_college_by_id(college_id):  # noqa: E501
    """Find college by ID

    Returns a single college # noqa: E501

    :param college_id: ID of college to return
    :type college_id: int

    :rtype: College
    """
    return 'do some magic!'


def update_college(body):  # noqa: E501
    """Update an existing college

     # noqa: E501

    :param body: College object that needs to be updated in the system
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = College.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
