import connexion
import six

from swagger_server.models.degree import Degree  # noqa: E501
from swagger_server import util

from sqlalchemy import types
from sqlalchemy import exc

def get_degree_by_id(degree_id):  # noqa: E501
    """Find degree by ID

    Returns a single degree # noqa: E501

    :param degree_id: ID of degree to return
    :type degree_id: int

    :rtype: Degree
    """
    select_string = """
                    SELECT * FROM degree
                    WHERE degree_id = "{}"
                    """.format(degree_id)
    try:
        result = connexion.DB.execute(select_string)
        for row in result:
            res = {
                'name': row["name"],
                'degree_id': row["degree_id"],
                'degree_type': row["degree_type"],
                'college_id': row["college_id"]
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
        db_conn = connexion.DB(connexion.DB_ENG)
        result = db_conn.execute(select_string)
        db_conn.close()
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
                        WHERE college_id = "{}"
                        """.format(college_id)
    try:
        db_conn = connexion.DB(connexion.DB_ENG)
        result = db_conn.execute(select_string)
        db_conn.close()
        for row in result:
            res = {
                'name': row["name"],
                'degree_id': row["degree_id"],
                'degree_type': row["degree_type"],
                'college_id': row["college_id"]
            }
            return res, 200
        return "Object not found", 404
    except exc.IntegrityError:
        return "Internal Server Error", 500