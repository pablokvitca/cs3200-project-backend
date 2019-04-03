import connexion
import six

from swagger_server.models.schedule_option import ScheduleOption  # noqa: E501
from swagger_server import util


def add_schedule_option(body):  # noqa: E501
    """Add a schedule_option to the classdeck

     # noqa: E501

    :param body: ScheduleOption object that needs to be added to the system
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = ScheduleOption.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_schedule_option(schedule_option_id):  # noqa: E501
    """Deletes a schedule_option

     # noqa: E501

    :param schedule_option_id: ScheduleOption id to delete
    :type schedule_option_id: int

    :rtype: None
    """
    return 'do some magic!'


def get_schedule_option_by_id(schedule_option_id):  # noqa: E501
    """Find schedule_option by ID

    Returns a single schedule_option # noqa: E501

    :param schedule_option_id: ID of schedule_option to return
    :type schedule_option_id: int

    :rtype: ScheduleOption
    """
    return 'do some magic!'


def get_schedule_option_by_nuid(nuid):  # noqa: E501
    """List schedule_option by NUID

    Returns the schedule_options related to the given NUID # noqa: E501

    :param nuid: nuid of the user related to the schedule_option to return
    :type nuid: int

    :rtype: None
    """
    return 'do some magic!'


def update_schedule_option(body):  # noqa: E501
    """Update an existing schedule_option

     # noqa: E501

    :param body: ScheduleOption object that needs to be updated in the system
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = ScheduleOption.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
