# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.section_restriction import SectionRestriction  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSectionRestrictionController(BaseTestCase):
    """SectionRestrictionController integration test stubs"""

    def test_add_section_restriction(self):
        """Test case for add_section_restriction

        Add a section_restriction to the classdeck
        """
        body = SectionRestriction()
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/section_restriction',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_section_restriction(self):
        """Test case for delete_section_restriction

        Deletes a section_restriction
        """
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/section_restriction/{type}/{crn}'.format(type='type_example', crn=99999),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_section_restriction_by_id(self):
        """Test case for get_section_restriction_by_id

        Find section_restriction by ID
        """
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/section_restriction/{type}/{crn}'.format(type='type_example', crn=99999),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_section_restriction(self):
        """Test case for update_section_restriction

        Update an existing section_restriction
        """
        body = SectionRestriction()
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/section_restriction',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
