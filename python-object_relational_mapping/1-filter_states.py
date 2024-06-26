#!/usr/bin/python3
"""

Module containing a script that list all states with added specifications

"""


import MySQLdb
import sys

if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()

    cur.execute(
        "SELECT * FROM states WHERE name Like 'N%' ORDER BY states.id ASC")

    rows = cur.fetchall()

    for row in rows:
        if row[1][0] == 'N':
            print(row)

    cur.close()
    db.close()
