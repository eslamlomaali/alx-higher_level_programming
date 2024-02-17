#!/usr/bin/python3
"""
Your script should take 4 arguments: mysql username, mysql password,
database name and state name searched
(no argument validation needed)

"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    current = db.cursor()
    current.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
                .format(sys.argv[4]))
    rs = current.fetchall()
    for r in rs:
        print(r)
    current.close()
    db.close()
