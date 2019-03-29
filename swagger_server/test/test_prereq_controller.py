# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.prereq import Prereq  # noqa: E501
from swagger_server.test import BaseTestCase


class TestPrereqController(BaseTestCase):
    """PrereqController integration test stubs"""

    def test_add_prereq_class(self):
        """Test case for add_prereq_class

        Add a prereq to the classdeck
        """
        body = Prereq()
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/prereq/class',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_add_prereq_degree(self):
        """Test case for add_prereq_degree

        Add a prereq to the classdeck
        """
        body = Prereq()
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/prereq/degree',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_prereq_class(self):
        """Test case for delete_prereq_class

        Deletes a prereq
        """
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/prereq/class/{prereq_group_id}/{class_dept}/{class_number}'.format(prereq_group_id=1, class_dept='class_dept_example', class_number=9999),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_prereq_degree(self):
        """Test case for delete_prereq_degree

        Deletes a prereq
        """
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/prereq/degree/{prereq_group_id}/{class_dept}/{class_number}'.format(prereq_group_id=1, class_dept='class_dept_example', class_number=9999),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_prereq_class_by_id(self):
        """Test case for get_prereq_class_by_id

        Find prereq by ID
        """
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/prereq/class/{prereq_group_id}/{class_dept}/{class_number}'.format(prereq_group_id=1, class_dept='class_dept_example', class_number=9999),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_prereq_degree_by_id(self):
        """Test case for get_prereq_degree_by_id

        Find prereq by ID
        """
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/prereq/degree/{prereq_group_id}/{class_dept}/{class_number}'.format(prereq_group_id=1, class_dept='class_dept_example', class_number=9999),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_prereq_class(self):
        """Test case for update_prereq_class

        Update an existing prereq
        """
        body = Prereq()
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/prereq/class',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_prereq_degree(self):
        """Test case for update_prereq_degree

        Update an existing prereq
        """
        body = Prereq()
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/prereq/degree',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
