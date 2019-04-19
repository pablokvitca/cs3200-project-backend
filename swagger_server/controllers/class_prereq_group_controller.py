import connexion
import six

from swagger_server.models.class_prereq_group import ClassPrereqGroup  # noqa: E501
from swagger_server import util

from sqlalchemy import types
from sqlalchemy import exc


class ClassPrereq(object):

    def __init__(self,
                 pgc_group_id, pgc_min_fulfilled_req,
                 pgc_parent_group_id, pgc_class_dept,
                 pgc_class_number, pc_class_dept,
                 pc_class_number, pc_id):
        self.id = pc_id
        self.class_dept = pc_class_dept
        self.class_number = pc_class_number

    def add_req(self,
                pgc_group_id, pgc_min_fulfilled_req,
                pgc_parent_group_id, pgc_class_dept,
                pgc_class_number, pc_class_dept,
                pc_class_number, pc_id):
        pass

    def to_dict(self):
        return {
            "id": self.id,
            "class_dept": self.class_dept,
            "class_number": self.class_number
        }

    def meets_prereqs(self, classes_taken):
        me = {
            "class_dept": self.class_dept,
            "class_number": self.class_number
        }
        return me in classes_taken


class Prereq(object):

    def __init__(self,
                 pgc_group_id, pgc_min_fulfilled_req,
                 pgc_parent_group_id, pgc_class_dept,
                 pgc_class_number, pc_class_dept, pc_class_number, pc_id):
        self.group_id = pgc_group_id
        self.min_fulfilled_req = pgc_min_fulfilled_req
        self.parent_group_id = pgc_parent_group_id
        self.class_dept = pgc_class_dept
        self.class_number = pgc_class_number
        self.reqs = []
        self.add_req(pgc_group_id, pgc_min_fulfilled_req,
                     pgc_parent_group_id, pgc_class_dept,
                     pgc_class_number, pc_class_dept, pc_class_number, pc_id)

    def add_req(self,
                pgc_group_id, pgc_min_fulfilled_req,
                pgc_parent_group_id, pgc_class_dept,
                pgc_class_number, pc_class_dept,
                pc_class_number, pc_id):
        if self.group_id == pgc_group_id:
            if not isinstance(pc_id, type(None)):
                self.reqs.append(ClassPrereq(pgc_group_id, pgc_min_fulfilled_req,
                                             pgc_parent_group_id, pgc_class_dept,
                                             pgc_class_number, pc_class_dept,
                                             pc_class_number, pc_id))
        else:
            if self.group_id == pgc_parent_group_id:
                found = False
                for r in self.reqs:
                    if isinstance(r, Prereq) and r.group_id == pgc_group_id:
                        found = True
                        r.reqs.append(ClassPrereq(pgc_group_id, pgc_min_fulfilled_req,
                                                  pgc_parent_group_id, pgc_class_dept,
                                                  pgc_class_number, pc_class_dept,
                                                  pc_class_number, pc_id))
                if not found:
                    self.reqs.append(Prereq(pgc_group_id, pgc_min_fulfilled_req,
                                            pgc_parent_group_id, pgc_class_dept,
                                            pgc_class_number, pc_class_dept,
                                            pc_class_number, pc_id))
            else:
                for r in self.reqs:
                    r.add_req(pgc_group_id, pgc_min_fulfilled_req,
                              pgc_parent_group_id, pgc_class_dept,
                              pgc_class_number, pc_class_dept,
                              pc_class_number, pc_id)

    def to_dict(self):
        if not isinstance(self.class_dept, type(None)) and not isinstance(self.class_number, type(None)):
            res = {
                "group_id": self.group_id,
                "min_fulfilled_req": self.min_fulfilled_req,
                "parent_group_id": self.parent_group_id,
                "class_dept": self.class_dept,
                "class_number": self.class_number,
                "reqs": []
            }
        else:
            res = {
                "group_id": self.group_id,
                "min_fulfilled_req": self.min_fulfilled_req,
                "parent_group_id": self.parent_group_id,
                "reqs": []
            }
        for r in self.reqs:
            res["reqs"].append(r.to_dict())
        return res

    def meets_prereqs(self, classes_taken):
        count_satisfied = 0
        for r in self.reqs:
            if r.meets_prereqs(classes_taken):
                count_satisfied += 1
        return count_satisfied >= self.min_fulfilled_req


def get_class_coreqs(class_department, class_number):
    select_string = """
                        SELECT
                            pgc.group_id AS group_id,
                            pgc.min_fulfilled_req AS min_fulfilled_req,
                            pgc.class_dept AS class_dept,
                            pgc.class_number AS class_number,
                            pc.class_dept AS pc_class_dept,
                            pc.class_number AS pc_class_number,
                            pc.id AS pc_id
                        FROM prereq_group_class AS pgc
                        LEFT OUTER JOIN prereq_class AS pc ON pgc.group_id = pc.group_id
                        WHERE pgc.class_dept = "{0}"
                          AND pgc.class_number = {1}
                          AND coreq_group = TRUE;
                        """.format(class_department, class_number)
    try:
        db_conn = connexion.DB(connexion.DB_ENG)
        result = db_conn.execute(select_string)
        db_conn.close()
        res = {}
        for row in result:
            if "reqs" not in res:
                res = {
                    "group_id": row["group_id"],
                    "min_fulfilled_req": row["min_fulfilled_req"],
                    "class_dept": row["class_dept"],
                    "class_number": row["class_number"],
                    "reqs": []
                }
            res["reqs"].append({
                    "class_dept": row["pc_class_dept"],
                    "class_number": row["pc_class_number"],
                    "id": row["pc_id"]
            })
        return res, 200
    except exc.IntegrityError:
        return "Internal Server Error", 500


def get_class_prereqs(class_department, class_number):  # noqa: E501
    """Lists prereqs for the given class

    Returns a prereqs for the given class # noqa: E501

    :param class_department: short code of the Department related to the Class related to the ClassPrereqGroup to return
    :type class_department: str
    :param class_number: number of the Class related to the ClassPrereqGroup to return
    :type class_number: int

    :rtype: None
    """
    try:
        res = get_class_prereqs_db(class_department, class_number)
        return res if isinstance(res, dict) else res.to_dict(), 200
    except exc.IntegrityError:
        return "Internal Server Error", 500


def get_class_prereqs_db(class_department, class_number):
    db_conn = connexion.DB_ENG.raw_connection()
    cursor = db_conn.cursor()
    cursor.callproc("select_prerequisites_recursive", [class_department, class_number])
    db_conn.close()
    res = {}
    for pgc_group_id, pgc_min_fulfilled_req, \
        pgc_parent_group_id, pgc_class_dept, pgc_class_number, \
        pc_class_dept, pc_class_number, pc_id \
            in cursor.fetchall():
        if isinstance(res, Prereq):
            res.add_req(pgc_group_id, pgc_min_fulfilled_req,
                        pgc_parent_group_id, pgc_class_dept, pgc_class_number,
                        pc_class_dept, pc_class_number, pc_id)
        else:
            res = Prereq(pgc_group_id, pgc_min_fulfilled_req,
                         pgc_parent_group_id, pgc_class_dept, pgc_class_number,
                         pc_class_dept, pc_class_number, pc_id)
    return res
