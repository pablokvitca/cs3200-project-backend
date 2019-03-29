# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.degree_prereq_group import DegreePrereqGroup  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDegreePrereqGroupController(BaseTestCase):
    """DegreePrereqGroupController integration test stubs"""

    def test_add_degree_prereq_group(self):
        """Test case for add_degree_prereq_group

        Add a degree_prereq_group to the classdeck
        """
        body = DegreePrereqGroup()
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/degree_prereq_group',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_degree_prereq_group(self):
        """Test case for delete_degree_prereq_group

        Deletes a degree_prereq_group
        """
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/degree_prereq_group/{degree_prereq_group_id}'.format(degree_prereq_group_id=1),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_degree_prereq_group_by_id(self):
        """Test case for get_degree_prereq_group_by_id

        Find degree_prereq_group by ID
        """
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/degree_prereq_group/{degree_prereq_group_id}'.format(degree_prereq_group_id=1),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_degree_prereq_group(self):
        """Test case for update_degree_prereq_group

        Update an existing degree_prereq_group
        """
        body = DegreePrereqGroup()
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/degree_prereq_group',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
