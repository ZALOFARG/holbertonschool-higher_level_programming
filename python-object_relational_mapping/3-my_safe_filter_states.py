#!/usr/bin/python3
"""this module will displays all values in the states
table of hbtn_0e_0_usa where name matches the argument
SQL injection safe
usage:
    ./3-my_filter_states.py <username>
                            <password>
                            <db>
                            <string searched>
"""

import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("""SELECT * FROM states""")
    query_rows = cur.fetchall()
    for row in query_rows:
        if row[1] == sys.argv[4]:
            print(row)
    cur.close()
    db.close()
