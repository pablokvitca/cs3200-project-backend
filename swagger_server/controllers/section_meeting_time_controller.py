import connexion
import six

from swagger_server.models.section_meeting_time import SectionMeetingTime  # noqa: E501
from swagger_server import util


def add_section_meeting_time(body):  # noqa: E501
    """Add a section_meeting_time to the classdeck

     # noqa: E501

    :param body: SectionMeetingTime object that needs to be added to the system
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = SectionMeetingTime.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_section_meeting_time(crn, start_time, end_time, meeting_days):  # noqa: E501
    """Deletes a section_meeting_time

     # noqa: E501

    :param crn: crn of related section of the sectionMettingTime to return
    :type crn: int
    :param start_time: start_time of the sectionMettingTime to return
    :type start_time: str
    :param end_time: end_time of the sectionMettingTime to return
    :type end_time: str
    :param meeting_days: meeting_days of the sectionMettingTime to return
    :type meeting_days: str

    :rtype: None
    """
    return 'do some magic!'


def get_section_meeting_time_by_id(crn, start_time, end_time, meeting_days):  # noqa: E501
    """Find section_meeting_time by ID

    Returns a single section_meeting_time # noqa: E501

    :param crn: crn of related section of the sectionMettingTime to return
    :type crn: int
    :param start_time: start_time of the sectionMettingTime to return
    :type start_time: str
    :param end_time: end_time of the sectionMettingTime to return
    :type end_time: str
    :param meeting_days: meeting_days of the sectionMettingTime to return
    :type meeting_days: str

    :rtype: SectionMeetingTime
    """
    return 'do some magic!'


def update_section_meeting_time(body):  # noqa: E501
    """Update an existing section_meeting_time

     # noqa: E501

    :param body: SectionMeetingTime object that needs to be updated in the system
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = SectionMeetingTime.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
