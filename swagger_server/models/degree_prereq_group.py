# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class DegreePrereqGroup(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, group_id: int=None, min_fulfilled_req: int=None, degree_id: int=None):  # noqa: E501
        """DegreePrereqGroup - a model defined in Swagger

        :param group_id: The group_id of this DegreePrereqGroup.  # noqa: E501
        :type group_id: int
        :param min_fulfilled_req: The min_fulfilled_req of this DegreePrereqGroup.  # noqa: E501
        :type min_fulfilled_req: int
        :param degree_id: The degree_id of this DegreePrereqGroup.  # noqa: E501
        :type degree_id: int
        """
        self.swagger_types = {
            'group_id': int,
            'min_fulfilled_req': int,
            'degree_id': int
        }

        self.attribute_map = {
            'group_id': 'group_id',
            'min_fulfilled_req': 'min_fulfilled_req',
            'degree_id': 'degree_id'
        }

        self._group_id = group_id
        self._min_fulfilled_req = min_fulfilled_req
        self._degree_id = degree_id

    @classmethod
    def from_dict(cls, dikt) -> 'DegreePrereqGroup':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DegreePrereqGroup of this DegreePrereqGroup.  # noqa: E501
        :rtype: DegreePrereqGroup
        """
        return util.deserialize_model(dikt, cls)

    @property
    def group_id(self) -> int:
        """Gets the group_id of this DegreePrereqGroup.


        :return: The group_id of this DegreePrereqGroup.
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id: int):
        """Sets the group_id of this DegreePrereqGroup.


        :param group_id: The group_id of this DegreePrereqGroup.
        :type group_id: int
        """
        if group_id is not None and group_id < 1:  # noqa: E501
            raise ValueError("Invalid value for `group_id`, must be a value greater than or equal to `1`")  # noqa: E501

        self._group_id = group_id

    @property
    def min_fulfilled_req(self) -> int:
        """Gets the min_fulfilled_req of this DegreePrereqGroup.


        :return: The min_fulfilled_req of this DegreePrereqGroup.
        :rtype: int
        """
        return self._min_fulfilled_req

    @min_fulfilled_req.setter
    def min_fulfilled_req(self, min_fulfilled_req: int):
        """Sets the min_fulfilled_req of this DegreePrereqGroup.


        :param min_fulfilled_req: The min_fulfilled_req of this DegreePrereqGroup.
        :type min_fulfilled_req: int
        """
        if min_fulfilled_req is not None and min_fulfilled_req < 1:  # noqa: E501
            raise ValueError("Invalid value for `min_fulfilled_req`, must be a value greater than or equal to `1`")  # noqa: E501

        self._min_fulfilled_req = min_fulfilled_req

    @property
    def degree_id(self) -> int:
        """Gets the degree_id of this DegreePrereqGroup.


        :return: The degree_id of this DegreePrereqGroup.
        :rtype: int
        """
        return self._degree_id

    @degree_id.setter
    def degree_id(self, degree_id: int):
        """Sets the degree_id of this DegreePrereqGroup.


        :param degree_id: The degree_id of this DegreePrereqGroup.
        :type degree_id: int
        """
        if degree_id is not None and degree_id < 1:  # noqa: E501
            raise ValueError("Invalid value for `degree_id`, must be a value greater than or equal to `1`")  # noqa: E501

        self._degree_id = degree_id
