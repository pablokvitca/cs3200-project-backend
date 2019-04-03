# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.pursued_degree import PursuedDegree  # noqa: E501
from swagger_server.test import BaseTestCase


class TestPursuedDegreeController(BaseTestCase):
    """PursuedDegreeController integration test stubs"""

    def test_add_pursued_degree(self):
        """Test case for add_pursued_degree

        Add a pursued_degree to the classdeck
        """
        body = PursuedDegree()
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/pursued_degree',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_pursued_degree(self):
        """Test case for delete_pursued_degree

        Deletes a pursued_degree
        """
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/pursued_degree/{nuid}/{degree_id}'.format(nuid=1, degree_id=1),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_pursued_degree_by_nuid(self):
        """Test case for get_pursued_degree_by_nuid

        List pursued_degree by NUID
        """
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/pursued_degree/{nuid}'.format(nuid=1),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
