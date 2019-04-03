import connexion
import six

from swagger_server.models.attribute import Attribute  # noqa: E501
from swagger_server import util


def get_attribute_by_name(attribute_name):  # noqa: E501
    """Find attribute by name

    Returns a single attribute # noqa: E501

    :param attribute_name: name of attribute to return
    :type attribute_name: str

    :rtype: Attribute
    """
    return 'do some magic!'


def list_attributes():  # noqa: E501
    """List all attributes

    Returns all attributes # noqa: E501


    :rtype: None
    """
    return 'do some magic!'
