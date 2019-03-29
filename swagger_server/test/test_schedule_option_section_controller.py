# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.schedule_option_section import ScheduleOptionSection  # noqa: E501
from swagger_server.test import BaseTestCase


class TestScheduleOptionSectionController(BaseTestCase):
    """ScheduleOptionSectionController integration test stubs"""

    def test_add_schedule_option_section(self):
        """Test case for add_schedule_option_section

        Add a schedule_option_section to the classdeck
        """
        body = ScheduleOptionSection()
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/schedule_option_section',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_schedule_option_section(self):
        """Test case for delete_schedule_option_section

        Deletes a schedule_option_section
        """
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/schedule_option_section/{schedule_id}/{crn}'.format(schedule_id=1, crn=99999),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_schedule_option_section_by_id(self):
        """Test case for get_schedule_option_section_by_id

        Find schedule_option_section by ID
        """
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/schedule_option_section/{schedule_id}/{crn}'.format(schedule_id=1, crn=99999),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_schedule_option_section(self):
        """Test case for update_schedule_option_section

        Update an existing schedule_option_section
        """
        body = ScheduleOptionSection()
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/schedule_option_section',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
