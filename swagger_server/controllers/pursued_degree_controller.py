import connexion
import six

from swagger_server.models.pursued_degree import PursuedDegree  # noqa: E501
from swagger_server import util


def add_pursued_degree(body):  # noqa: E501
    """Add a pursued_degree to the classdeck

     # noqa: E501

    :param body: PursuedDegree object that needs to be added to the system
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PursuedDegree.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_pursued_degree(nuid, degree_id):  # noqa: E501
    """Deletes a pursued_degree

     # noqa: E501

    :param nuid: nuid of the user related to the pursued_degree to return
    :type nuid: int
    :param degree_id: nuid of the degree related to the pursued_degree to return
    :type degree_id: int

    :rtype: None
    """
    return 'do some magic!'


def get_pursued_degree_by_id(nuid, degree_id):  # noqa: E501
    """Find pursued_degree by ID

    Returns a single pursued_degree # noqa: E501

    :param nuid: nuid of the user related to the pursued_degree to return
    :type nuid: int
    :param degree_id: nuid of the degree related to the pursued_degree to return
    :type degree_id: int

    :rtype: PursuedDegree
    """
    return 'do some magic!'


def update_pursued_degree(body):  # noqa: E501
    """Update an existing pursued_degree

     # noqa: E501

    :param body: PursuedDegree object that needs to be updated in the system
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PursuedDegree.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
