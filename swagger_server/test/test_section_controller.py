# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.section import Section  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSectionController(BaseTestCase):
    """SectionController integration test stubs"""

    def test_add_section(self):
        """Test case for add_section

        Add a section to the classdeck
        """
        body = Section()
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/section',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_section(self):
        """Test case for delete_section

        Deletes a section
        """
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/section/{crn}'.format(crn=99999),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_section_by_crn(self):
        """Test case for get_section_by_crn

        Find section by
        """
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/section/{crn}'.format(crn=99999),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_section(self):
        """Test case for update_section

        Update an existing section
        """
        body = Section()
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/section',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
