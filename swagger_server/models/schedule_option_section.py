# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ScheduleOptionSection(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, schedule_id: int=None, crn: int=None):  # noqa: E501
        """ScheduleOptionSection - a model defined in Swagger

        :param schedule_id: The schedule_id of this ScheduleOptionSection.  # noqa: E501
        :type schedule_id: int
        :param crn: The crn of this ScheduleOptionSection.  # noqa: E501
        :type crn: int
        """
        self.swagger_types = {
            'schedule_id': int,
            'crn': int
        }

        self.attribute_map = {
            'schedule_id': 'schedule_id',
            'crn': 'crn'
        }

        self._schedule_id = schedule_id
        self._crn = crn

    @classmethod
    def from_dict(cls, dikt) -> 'ScheduleOptionSection':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ScheduleOptionSection of this ScheduleOptionSection.  # noqa: E501
        :rtype: ScheduleOptionSection
        """
        return util.deserialize_model(dikt, cls)

    @property
    def schedule_id(self) -> int:
        """Gets the schedule_id of this ScheduleOptionSection.


        :return: The schedule_id of this ScheduleOptionSection.
        :rtype: int
        """
        return self._schedule_id

    @schedule_id.setter
    def schedule_id(self, schedule_id: int):
        """Sets the schedule_id of this ScheduleOptionSection.


        :param schedule_id: The schedule_id of this ScheduleOptionSection.
        :type schedule_id: int
        """
        if schedule_id is not None and schedule_id < 0:  # noqa: E501
            raise ValueError("Invalid value for `schedule_id`, must be a value greater than or equal to `0`")  # noqa: E501

        self._schedule_id = schedule_id

    @property
    def crn(self) -> int:
        """Gets the crn of this ScheduleOptionSection.


        :return: The crn of this ScheduleOptionSection.
        :rtype: int
        """
        return self._crn

    @crn.setter
    def crn(self, crn: int):
        """Sets the crn of this ScheduleOptionSection.


        :param crn: The crn of this ScheduleOptionSection.
        :type crn: int
        """
        if crn is not None and crn > 99999:  # noqa: E501
            raise ValueError("Invalid value for `crn`, must be a value less than or equal to `99999`")  # noqa: E501
        if crn is not None and crn < 0:  # noqa: E501
            raise ValueError("Invalid value for `crn`, must be a value greater than or equal to `0`")  # noqa: E501

        self._crn = crn
