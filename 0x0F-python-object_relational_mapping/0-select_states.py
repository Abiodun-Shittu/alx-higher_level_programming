#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys


if __name__ == '__main__':
    HOST = 'localhost'
    PORT = 3306
    USERNAME = sys.argv[1]
    PASSWORD = sys.argv[2]
    DATABASE = sys.argv[3]

    db = MySQLdb.connect(HOST, PORT, USERNAME, PASSWORD, DATABASE)

    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    table = cur.fetchall()

    for row in table:
        print(row)

    cur.close()
    db.close()
