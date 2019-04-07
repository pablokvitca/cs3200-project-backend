import connexion
import six

from swagger_server.models.degree import Degree  # noqa: E501
from swagger_server import util

from sqlalchemy import types
from sqlalchemy import exc


def add_degree(body):  # noqa: E501
    """Add a degree to the classdeck

     # noqa: E501

    :param body: Degree object that needs to be added to the system
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Degree.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def degree_list_prereqs(degree_id):  # noqa: E501
    """List the prereqs for a given degree

     # noqa: E501

    :param degree_id: Degree id to delete
    :type degree_id: int

    :rtype: None
    """
    return "do some magic!"


def delete_degree(degree_id):  # noqa: E501
    """Deletes a degree

     # noqa: E501

    :param degree_id: Degree id to delete
    :type degree_id: int

    :rtype: None
    """
    return 'do some magic!'


def get_degree_by_id(degree_id):  # noqa: E501
    """Find degree by ID

    Returns a single degree # noqa: E501

    :param degree_id: ID of degree to return
    :type degree_id: int

    :rtype: Degree
    """
    select_string = """
                    SELECT * FROM degree
                    WHERE degree_ID = "{}"
                    """.format(degree_id)
    try:
        result = connexion.DB.execute(select_string)
        for row in result:
            res = {
                'name': row["name"],
                'degree_ID': row["degree_ID"],
                'degree_type': row["degree_type"],
                'college_ID': row["college_ID"]
            }
            return res, 200
        return "Object not found", 404
    except exc.IntegrityError:
        return "Internal Server Error", 500


def list_degrees():  # noqa: E501
    """List all degrees

     # noqa: E501


    :rtype: None
    """

    select_string = """
            SELECT * FROM degree;
            """
    try:
        result = connexion.DB.execute(select_string)
        res = []
        for name, degree_id, degree_type, college_id in result.fetchall():
            r = Degree(degree_id, name, college_id, degree_type)
            res.append(r)
        return res, 200
    except exc.IntegrityError:
        return "Internal Server Error", 500


def list_degrees_by_college(college_id):  # noqa: E501
    """List all degrees in the given college

     # noqa: E501

    :param college_id: ID of college related to the degrees to return
    :type college_id: int

    :rtype: None
    """
    select_string = """
                        SELECT * FROM degree
                        WHERE college_ID = "{}"
                        """.format(college_id)
    try:
        result = connexion.DB.execute(select_string)
        for row in result:
            res = {
                'name': row["name"],
                'degree_ID': row["degree_ID"],
                'degree_type': row["degree_type"],
                'college_ID': row["college_ID"]
            }
            return res, 200
        return "Object not found", 404
    except exc.IntegrityError:
        return "Internal Server Error", 500


def update_degree(body):  # noqa: E501
    """Update an existing degree

     # noqa: E501

    :param body: Degree object that needs to be updated in the system
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Degree.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
