import connexion
import six

from swagger_server.models.department import Department  # noqa: E501
from swagger_server import util


from sqlalchemy import types
from sqlalchemy import exc


def get_department_by_short_code(department_short_code):  # noqa: E501
    """Find department by short code

    Returns a single department # noqa: E501

    :param department_short_code: short code of department to return
    :type department_short_code: str

    :rtype: Department
    """
    select_string = """
            SELECT * FROM department
            WHERE short_name = "{}"
            """.format(department_short_code)
    try:
        result = connexion.DB.execute(select_string)
        for row in result:
            res = {
                'short_name': row["short_name"],
                'long_name': row["long_name"],
                'college_id': row["college_id"]
            }
            return res, 200
        return "Object not found", 404
    except exc.IntegrityError:
        return "Internal Server Error", 500


def list_department():  # noqa: E501
    """List all departments

     # noqa: E501


    :rtype: None
    """
    select_string = """
            SELECT * FROM department
            """
    try:
        result = connexion.DB.execute(select_string)
        res = []
        for row in result:
            r = Department.from_dict(row)
            res.append({
                'short_name': row["short_name"],
                'long_name': row["long_name"],
                'college_id': row["college_id"]
            })
        return res, 200
    except exc.IntegrityError:
        return "Internal Server Error", 500
