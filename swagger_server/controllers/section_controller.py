import connexion
import six

from swagger_server.models.section import Section  # noqa: E501
from swagger_server import util


def add_section(body):  # noqa: E501
    """Add a section to the classdeck

     # noqa: E501

    :param body: Section object that needs to be added to the system
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Section.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_section(crn):  # noqa: E501
    """Deletes a section

     # noqa: E501

    :param crn: Section CRN to delete
    :type crn: int

    :rtype: None
    """
    return 'do some magic!'


def get_section_by_crn(crn):  # noqa: E501
    """Find section by

    Returns a single section # noqa: E501

    :param crn: CRN of section to return
    :type crn: int

    :rtype: Section
    """
    return 'do some magic!'


def update_section(body):  # noqa: E501
    """Update an existing section

     # noqa: E501

    :param body: Section object that needs to be updated in the system
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Section.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
