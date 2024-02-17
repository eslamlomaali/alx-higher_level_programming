#!/usr/bin/python3
"""
write a script that takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument
But this time, write one that is safe from MySQL injections!

"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    current = db.cursor()
    att = sys.argv[4]
    current.execute("SELECT * FROM states WHERE name LIKE %s", (att, ))
    rs = current.fetchall()
    for r in rs:
        print(r)
    current.close()
    db.close()
