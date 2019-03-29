# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.schedule_option import ScheduleOption  # noqa: E501
from swagger_server.test import BaseTestCase


class TestScheduleOptionController(BaseTestCase):
    """ScheduleOptionController integration test stubs"""

    def test_add_schedule_option(self):
        """Test case for add_schedule_option

        Add a schedule_option to the classdeck
        """
        body = ScheduleOption()
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/schedule_option',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_schedule_option(self):
        """Test case for delete_schedule_option

        Deletes a schedule_option
        """
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/schedule_option/{schedule_option_id}'.format(schedule_option_id=1),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_schedule_option_by_id(self):
        """Test case for get_schedule_option_by_id

        Find schedule_option by ID
        """
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/schedule_option/{schedule_option_id}'.format(schedule_option_id=1),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_schedule_option(self):
        """Test case for update_schedule_option

        Update an existing schedule_option
        """
        body = ScheduleOption()
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/schedule_option',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
