import connexion
import six

from swagger_server.models.attribute import Attribute  # noqa: E501
from swagger_server import util


def add_attribute(body):  # noqa: E501
    """Add a attribute to the classdeck

     # noqa: E501

    :param body: Attribute object that needs to be added to the system
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Attribute.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_attribute(attribute_name):  # noqa: E501
    """Deletes a attribute

     # noqa: E501

    :param attribute_name: name of the attribute to delete
    :type attribute_name: str

    :rtype: None
    """
    return 'do some magic!'


def get_attribute_by_name(attribute_name):  # noqa: E501
    """Find attribute by name

    Returns a single attribute # noqa: E501

    :param attribute_name: name of attribute to return
    :type attribute_name: str

    :rtype: Attribute
    """
    return 'do some magic!'


def update_attribute(body):  # noqa: E501
    """Update an existing attribute

     # noqa: E501

    :param body: Attribute object that needs to be updated in the system
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Attribute.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
