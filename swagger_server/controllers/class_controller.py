import connexion
import six

from swagger_server.models.model_class import ModelClass  # noqa: E501
from swagger_server import util


def add_class(body):  # noqa: E501
    """Add a class to the classdeck

     # noqa: E501

    :param body: Class object that needs to be added to the system
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = ModelClass.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_class_by_id(class_department, class_number):  # noqa: E501
    """Find class by ID

    Returns a single class # noqa: E501

    :param class_department: short code of the department that offers the class to return
    :type class_department: str
    :param class_number: class number of the class to return
    :type class_number: int

    :rtype: ModelClass
    """
    return 'do some magic!'


def list_classes():  # noqa: E501
    """List all classes

    Returns all classes # noqa: E501


    :rtype: None
    """
    return 'do some magic!'
