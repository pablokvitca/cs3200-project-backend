import connexion
import six

from swagger_server.models.college import College  # noqa: E501
from swagger_server import util


from sqlalchemy import types
from sqlalchemy import exc

def get_college_by_id(college_id):  # noqa: E501
    """Find college by ID

    Returns a single college # noqa: E501

    :param college_id: ID of college to return
    :type college_id: int

    :rtype: College
    """
    select_string = """
                SELECT * FROM college
                WHERE ID = "{}"
                """.format(college_id)
    try:
        result = connexion.DB.execute(select_string)
        for row in result:
            res = {
                'name': row["name"],
                'ID': row["ID"]
            }
            return res, 200
        return "Object not found", 404
    except exc.IntegrityError:
        return "Internal Server Error", 500


def list_colleges():  # noqa: E501
    """List all colleges

    Returns all colleges # noqa: E501

    :param college_id: ID of college to return
    :type college_id: int

    :rtype: None
    """
    select_string = """
                SELECT * FROM college
                """
    try:
        result = connexion.DB.execute(select_string)
        res = []
        for row in result:
            r = College.from_dict(row)
            res.append({
                'name': row["name"],
                'id': row["id"],
            })
        return res, 200
    except exc.IntegrityError:
        return "Internal Server Error", 500