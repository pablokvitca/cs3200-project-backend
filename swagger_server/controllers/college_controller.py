import connexion
import six

from swagger_server.models.college import College  # noqa: E501
from swagger_server import util


def get_college_by_id(college_id):  # noqa: E501
    """Find college by ID

    Returns a single college # noqa: E501

    :param college_id: ID of college to return
    :type college_id: int

    :rtype: College
    """
    return 'do some magic!'


def list_colleges(college_id):  # noqa: E501
    """List all colleges

    Returns all colleges # noqa: E501

    :param college_id: ID of college to return
    :type college_id: int

    :rtype: None
    """
    return 'do some magic!'
