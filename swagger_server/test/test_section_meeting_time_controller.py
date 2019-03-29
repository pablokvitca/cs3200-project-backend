# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.section_meeting_time import SectionMeetingTime  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSectionMeetingTimeController(BaseTestCase):
    """SectionMeetingTimeController integration test stubs"""

    def test_add_section_meeting_time(self):
        """Test case for add_section_meeting_time

        Add a section_meeting_time to the classdeck
        """
        body = SectionMeetingTime()
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/section_meeting_time',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_section_meeting_time(self):
        """Test case for delete_section_meeting_time

        Deletes a section_meeting_time
        """
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/section_meeting_time/{crn}/{start_time}/{end_time}/{meeting_days}'.format(crn=99999, start_time='start_time_example', end_time='end_time_example', meeting_days='meeting_days_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_section_meeting_time_by_id(self):
        """Test case for get_section_meeting_time_by_id

        Find section_meeting_time by ID
        """
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/section_meeting_time/{crn}/{start_time}/{end_time}/{meeting_days}'.format(crn=99999, start_time='start_time_example', end_time='end_time_example', meeting_days='meeting_days_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_section_meeting_time(self):
        """Test case for update_section_meeting_time

        Update an existing section_meeting_time
        """
        body = SectionMeetingTime()
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/section_meeting_time',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
