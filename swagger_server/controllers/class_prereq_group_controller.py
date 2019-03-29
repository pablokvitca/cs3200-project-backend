import connexion
import six

from swagger_server.models.class_prereq_group import ClassPrereqGroup  # noqa: E501
from swagger_server import util


def add_class_prereq_group(body):  # noqa: E501
    """Add a class_prereq_group to the classdeck

     # noqa: E501

    :param body: ClassPrereqGroup object that needs to be added to the system
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = ClassPrereqGroup.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_class_prereq_group(class_prereq_group_id):  # noqa: E501
    """Deletes a class_prereq_group

     # noqa: E501

    :param class_prereq_group_id: ClassPrereqGroup id to delete
    :type class_prereq_group_id: int

    :rtype: None
    """
    return 'do some magic!'


def get_class_prereq_group_by_id(class_prereq_group_id):  # noqa: E501
    """Find class_prereq_group by ID

    Returns a single class_prereq_group # noqa: E501

    :param class_prereq_group_id: ID of class_prereq_group to return
    :type class_prereq_group_id: int

    :rtype: ClassPrereqGroup
    """
    return 'do some magic!'


def update_class_prereq_group(body):  # noqa: E501
    """Update an existing class_prereq_group

     # noqa: E501

    :param body: ClassPrereqGroup object that needs to be updated in the system
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = ClassPrereqGroup.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
