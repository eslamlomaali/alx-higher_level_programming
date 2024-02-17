#!/usr/bin/python3


import MySQLdb
from sys import argv

'''
Write a script that lists all states from the database hbtn_0e_0_usa:
'''
if __name__ == "__main__":
    connectaion = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1],
        password=argv[2], database=argv[3])
    cur = connectaion.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    daba = cur.fetchall()
    for x in daba:
        print(x)
    cur.close()
    daba.close()
