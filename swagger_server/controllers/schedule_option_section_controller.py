import connexion
import six

from swagger_server.models.schedule_option_section import ScheduleOptionSection  # noqa: E501
from swagger_server import util


def add_schedule_option_section(body):  # noqa: E501
    """Add a schedule_option_section to the classdeck

     # noqa: E501

    :param body: ScheduleOptionSection object that needs to be added to the system
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = ScheduleOptionSection.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_schedule_option_section(schedule_id, crn):  # noqa: E501
    """Deletes a schedule_option_section

     # noqa: E501

    :param schedule_id: ID of the schedule related to the schedule_option_section to return
    :type schedule_id: int
    :param crn: crn of the section related to the schedule_option_section to return
    :type crn: int

    :rtype: None
    """
    return 'do some magic!'


def get_schedule_option_section_by_id(schedule_id, crn):  # noqa: E501
    """Find schedule_option_section by ID

    Returns a single schedule_option_section # noqa: E501

    :param schedule_id: ID of the schedule related to the schedule_option_section to return
    :type schedule_id: int
    :param crn: crn of the section related to the schedule_option_section to return
    :type crn: int

    :rtype: ScheduleOptionSection
    """
    return 'do some magic!'


def update_schedule_option_section(body):  # noqa: E501
    """Update an existing schedule_option_section

     # noqa: E501

    :param body: ScheduleOptionSection object that needs to be updated in the system
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = ScheduleOptionSection.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
