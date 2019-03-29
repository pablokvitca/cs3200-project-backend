import connexion
import six

from swagger_server.models.prereq import Prereq  # noqa: E501
from swagger_server import util


def add_prereq_class(body):  # noqa: E501
    """Add a prereq to the classdeck

     # noqa: E501

    :param body: Prereq object that needs to be added to the system
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Prereq.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def add_prereq_degree(body):  # noqa: E501
    """Add a prereq to the classdeck

     # noqa: E501

    :param body: Prereq object that needs to be added to the system
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Prereq.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_prereq_class(prereq_group_id, class_dept, class_number):  # noqa: E501
    """Deletes a prereq

     # noqa: E501

    :param prereq_group_id: ID of prereq group related to the prereq to return
    :type prereq_group_id: int
    :param class_dept: short code of the department of the class related to the prereq to return
    :type class_dept: str
    :param class_number: number of the class related to the prereq to return
    :type class_number: int

    :rtype: None
    """
    return 'do some magic!'


def delete_prereq_degree(prereq_group_id, class_dept, class_number):  # noqa: E501
    """Deletes a prereq

     # noqa: E501

    :param prereq_group_id: ID of prereq group related to the prereq to return
    :type prereq_group_id: int
    :param class_dept: short code of the department of the class related to the prereq to return
    :type class_dept: str
    :param class_number: number of the class related to the prereq to return
    :type class_number: int

    :rtype: None
    """
    return 'do some magic!'


def get_prereq_class_by_id(prereq_group_id, class_dept, class_number):  # noqa: E501
    """Find prereq by ID

    Returns a single prereq # noqa: E501

    :param prereq_group_id: ID of prereq group related to the prereq to return
    :type prereq_group_id: int
    :param class_dept: short code of the department of the class related to the prereq to return
    :type class_dept: str
    :param class_number: number of the class related to the prereq to return
    :type class_number: int

    :rtype: Prereq
    """
    return 'do some magic!'


def get_prereq_degree_by_id(prereq_group_id, class_dept, class_number):  # noqa: E501
    """Find prereq by ID

    Returns a single prereq # noqa: E501

    :param prereq_group_id: ID of prereq group related to the prereq to return
    :type prereq_group_id: int
    :param class_dept: short code of the department of the class related to the prereq to return
    :type class_dept: str
    :param class_number: number of the class related to the prereq to return
    :type class_number: int

    :rtype: Prereq
    """
    return 'do some magic!'


def update_prereq_class(body):  # noqa: E501
    """Update an existing prereq

     # noqa: E501

    :param body: Prereq object that needs to be updated in the system
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Prereq.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_prereq_degree(body):  # noqa: E501
    """Update an existing prereq

     # noqa: E501

    :param body: Prereq object that needs to be updated in the system
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Prereq.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
