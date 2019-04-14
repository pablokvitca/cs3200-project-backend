import connexion
import six

from swagger_server.models.semester import Semester  # noqa: E501
from swagger_server import util


def list_semesters():
    select_string = "SELECT * FROM semester;"
    db_conn = connexion.DB(connexion.DB_ENG)
    result = db_conn.execute(select_string)
    db_conn.close()
    res = []
    for id, year, semester in result.fetchall():
        r = {
            "id": id,
            "year": year,
            "semester": semester
        }
        res.append(r)
    return res, 200

