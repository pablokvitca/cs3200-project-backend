# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.class_prereq_group import ClassPrereqGroup  # noqa: E501
from swagger_server.test import BaseTestCase


class TestClassPrereqGroupController(BaseTestCase):
    """ClassPrereqGroupController integration test stubs"""

    def test_get_class_prereq_group_by_id(self):
        """Test case for get_class_prereq_group_by_id

        Find class_prereq_group by ID
        """
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/class_prereq_group/{class_prereq_group_id}'.format(class_prereq_group_id=1),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_class_prereqs(self):
        """Test case for get_class_prereqs

        Lists prereqs for the given class
        """
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/class_prereq_group/{class_department}/{class_number}'.format(class_department='class_department_example', class_number=9999),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
