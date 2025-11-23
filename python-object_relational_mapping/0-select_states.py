#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Komanda sətrindən arqumentləri oxuyuruq
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    # MySQL serverinə qoşuluruq
    conn = MySQLdb.connect(host="localhost", port=3306, user=user, passwd=passwd, db=db_name)
    cur = conn.cursor()

    # states cədvəlindən bütün məlumatları id üzrə artan sıra ilə götürürük
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()

    # Nəticələri çap edirik
    for row in rows:
        print(row)

    # Bağlantını bağlayırıq
    cur.close()
    conn.close()
