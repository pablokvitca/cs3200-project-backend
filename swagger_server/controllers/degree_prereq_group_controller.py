import connexion
import six

from swagger_server.models.degree_prereq_group import DegreePrereqGroup  # noqa: E501
from swagger_server import util


def add_degree_prereq_group(body):  # noqa: E501
    """Add a degree_prereq_group to the classdeck

     # noqa: E501

    :param body: DegreePrereqGroup object that needs to be added to the system
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = DegreePrereqGroup.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_degree_prereq_group(degree_prereq_group_id):  # noqa: E501
    """Deletes a degree_prereq_group

     # noqa: E501

    :param degree_prereq_group_id: DegreePrereqGroup id to delete
    :type degree_prereq_group_id: int

    :rtype: None
    """
    return 'do some magic!'


def get_degree_prereq_group_by_id(degree_prereq_group_id):  # noqa: E501
    """Find degree_prereq_group by ID

    Returns a single degree_prereq_group # noqa: E501

    :param degree_prereq_group_id: ID of degree_prereq_group to return
    :type degree_prereq_group_id: int

    :rtype: DegreePrereqGroup
    """
    return 'do some magic!'


def update_degree_prereq_group(body):  # noqa: E501
    """Update an existing degree_prereq_group

     # noqa: E501

    :param body: DegreePrereqGroup object that needs to be updated in the system
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = DegreePrereqGroup.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
