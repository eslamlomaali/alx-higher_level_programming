#!/usr/bin/python3
"""
Write a script that takes in the name of a state as an
argument and lists all citiesof that state, using the database hbtn_0e_4_usa

"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    current = db.cursor()
    current.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (sys.argv[4],))
    rs = current.fetchall()
    def = list(r[0] for r in rs)
    print(*def, sep=", ")
    current.close()
    db.close()
