#!/usr/bin/python3
"""
Displays all values in the states table where name matches
the argument provided by the user.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=passwd,
        db=db_name
    )
    cur = conn.cursor()

    # Query with format to safely insert user input
    query = ("SELECT * FROM states "
             "WHERE name = '{}' "
             "ORDER BY id ASC").format(state_name)
    cur.execute(query)
    rows = cur.fetchall()

    # Print results
    for row in rows:
        print(row)

    cur.close()
    conn.close()
