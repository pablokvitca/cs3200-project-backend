import connexion
import six

from swagger_server.models.class_prereq_group import ClassPrereqGroup  # noqa: E501
from swagger_server import util


def get_class_prereq_group_by_id(class_prereq_group_id):  # noqa: E501
    """Find class_prereq_group by ID

    Returns a single class_prereq_group # noqa: E501

    :param class_prereq_group_id: ID of class_prereq_group to return
    :type class_prereq_group_id: int

    :rtype: ClassPrereqGroup
    """
    return 'do some magic!'


def get_class_prereqs(class_department, class_number):  # noqa: E501
    """Lists prereqs for the given class

    Returns a prereqs for the given class # noqa: E501

    :param class_department: short code of the Department related to the Class related to the ClassPrereqGroup to return
    :type class_department: str
    :param class_number: number of the Class related to the ClassPrereqGroup to return
    :type class_number: int

    :rtype: None
    """
    return 'do some magic!'
