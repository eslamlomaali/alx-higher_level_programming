#!/usr/bin/python3
"""  Write a script that lists all states from the database hbtn_0e_0_usa: """
import MySQLdb
import sys


if __name__ == "__main__":
    daba = MySQLdb.connect(host="localhost", username=sys.argv[1],
                         password=sys.argv[2], daba=sys.argv[3], port=3306)
    current = daba.cursor()
    current.execute("SELECT * FROM states")
    r = current.fetchall()
    for rows in r:
        print(rows)
    current.close()
    daba.close()
