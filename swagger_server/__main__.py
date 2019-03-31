#!/usr/bin/env python3

import connexion

from swagger_server import encoder

import sqlalchemy
from sqlalchemy import create_engine

import json

settings = {
    # The name of the MySQL account to use (or empty for anonymous)
    'userName': "root",
    # The password for the MySQL account (or empty for anonymous)
    'password': "rycbar12345",
    'serverName': "127.0.0.1",    # The name of the computer running MySQL
    # The port of the MySQL server (default is 3306)
    'portNumber': 3306,
    # The name of the database we are testing with (this default is installed with MySQL)
    'dbName': "projectcs3200",
}


def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'ClassDeck Project'})
    connexion.DB = connect_db()
    connexion.verify_JWT = verify_JWT
    app.run(port=8080)


def verify_JWT(cookie):
    """If the user is log in is valid, then returns the user id
    else, returns False
    """
    if (cookie == 'logged_out'):
        return False

    session = json.loads(cookie)
    encoded = jwt_encode(session["nuid"])
    if (encoded == session["jwt"]):
        return session["nuid"]
    else:
        return False


def jwt_encode(target):
    """Encodes the given target using some encryption
    not to be disclosed.
    """
    return "secret"  # TODO: actually encode


def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'db_conn'):
        g.db_conn = connect_db()
    return g.db_conn


def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'db_conn'):
        g.db_conn.close()


def connect_db():
    print('Trying to connect to database')
    db_engine = create_engine(
        'mysql+mysqldb://{0[userName]}:{0[password]}@{0[serverName]}:{0[portNumber]}/{0[dbName]}'.format(settings))
    db_conn = db_engine.connect()
    print('Connected to database')
    return db_conn


if __name__ == '__main__':
    main()
