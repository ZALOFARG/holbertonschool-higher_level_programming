#!/usr/bin/python3
"""this module will lists all cities from a DB
    usage:
    ./4-my_filter_states.py <username>
                            <password>
                            <db>
"""

import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name FROM cities
            INNER JOIN states ON cities.state_id = states.id
            ORDER BY id ASC""")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
