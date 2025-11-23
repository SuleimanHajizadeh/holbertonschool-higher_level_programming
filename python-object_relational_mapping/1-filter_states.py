#!/usr/bin/python3
"""
Lists all states with a name starting with N
from the database hbtn_0e_0_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL server
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=passwd,
        db=db_name
    )
    cur = conn.cursor()

    # Case-insensitive query using UPPER()
    cur.execute("SELECT * FROM states WHERE UPPER(name) LIKE 'N%' ORDER BY id ASC")
    rows = cur.fetchall()

    # Print results
    for row in rows:
        print(row)

    cur.close()
    conn.close()
