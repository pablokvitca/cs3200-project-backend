import connexion
import six

from swagger_server.models.class_attribute import ClassAttribute  # noqa: E501
from swagger_server import util


def add_class_attribute(body):  # noqa: E501
    """Add a class_attribute to the classdeck

     # noqa: E501

    :param body: ClassAttribute object that needs to be added to the system
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = ClassAttribute.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_class_attribute(attribute_name, class_department, class_number):  # noqa: E501
    """Deletes a class_attribute

     # noqa: E501

    :param attribute_name: name of the Attribute related to the ClassAttribute to delete
    :type attribute_name: str
    :param class_department: short code of the Department related to the Class related to the ClassAttribute to delete
    :type class_department: str
    :param class_number: number of the Class related to the ClassAttribute to delete
    :type class_number: int

    :rtype: None
    """
    return 'do some magic!'


def get_class_attribute_by_id(attribute_name, class_department, class_number):  # noqa: E501
    """Find class_attribute by ID

    Returns a single class_attribute # noqa: E501

    :param attribute_name: name of the Attribute related to the ClassAttribute to return
    :type attribute_name: str
    :param class_department: short code of the Department related to the Class related to the ClassAttribute to return
    :type class_department: str
    :param class_number: number of the Class related to the ClassAttribute to return
    :type class_number: int

    :rtype: ClassAttribute
    """
    return 'do some magic!'


def update_class_attribute(body):  # noqa: E501
    """Update an existing class_attribute

     # noqa: E501

    :param body: ClassAttribute object that needs to be updated in the system
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = ClassAttribute.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
