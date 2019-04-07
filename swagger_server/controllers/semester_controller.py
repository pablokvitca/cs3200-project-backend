import connexion
import six

from swagger_server.models.semester import Semester  # noqa: E501
from swagger_server import util


def list_semesters():
    select_string = "SELECT * FROM semester;"
    result = connexion.DB.execute(select_string)
    res = []
    for id, year, semester in result.fetchall():
        r = {
            "id": id,
            "year": year,
            "semester": semester
        }
        res.append(r)
    return res, 200

