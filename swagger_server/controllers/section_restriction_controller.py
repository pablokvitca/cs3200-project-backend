import connexion
import six

from swagger_server.models.section_restriction import SectionRestriction  # noqa: E501
from swagger_server import util


def add_section_restriction(body):  # noqa: E501
    """Add a section_restriction to the classdeck

     # noqa: E501

    :param body: SectionRestriction object that needs to be added to the system
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = SectionRestriction.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_section_restriction(type, crn):  # noqa: E501
    """Deletes a section_restriction

     # noqa: E501

    :param type: type of the section_restriction to return
    :type type: str
    :param crn: crn of the section_restriction to return
    :type crn: int

    :rtype: None
    """
    return 'do some magic!'


def get_section_restriction_by_id(type, crn):  # noqa: E501
    """Find section_restriction by ID

    Returns a single section_restriction # noqa: E501

    :param type: type of the section_restriction to return
    :type type: str
    :param crn: crn of the section_restriction to return
    :type crn: int

    :rtype: SectionRestriction
    """
    return 'do some magic!'


def update_section_restriction(body):  # noqa: E501
    """Update an existing section_restriction

     # noqa: E501

    :param body: SectionRestriction object that needs to be updated in the system
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = SectionRestriction.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
