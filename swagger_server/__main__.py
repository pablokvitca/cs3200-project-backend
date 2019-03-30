#!/usr/bin/env python3

import connexion

from swagger_server import encoder

import sqlalchemy
from sqlalchemy import create_engine

settings = {
    'userName': "root",           # The name of the MySQL account to use (or empty for anonymous)
    'password': "WRITE PASSWORD HERE",           # The password for the MySQL account (or empty for anonymous)
    'serverName': "127.0.0.1",    # The name of the computer running MySQL
    'portNumber': 3306,           # The port of the MySQL server (default is 3306)
    'dbName': "projectcs3200",             # The name of the database we are testing with (this default is installed with MySQL)
}

def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'ClassDeck Project'})
    connexion.DB = connect_db()
    app.run(port=8080)

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
    db_engine = create_engine('mysql+mysqldb://{0[userName]}:{0[password]}@{0[serverName]}:{0[portNumber]}/{0[dbName]}'.format(settings))
    db_conn = db_engine.connect()
    print('Connected to database')
    return db_conn

if __name__ == '__main__':
    main()