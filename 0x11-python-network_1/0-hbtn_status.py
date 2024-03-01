#!/usr/bin/python3
"""Write a Python script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request


if __name__ == '__main__':
        with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as ans:
            master = ans.read()
            print("Body response:")
            print("\t- type: {}".format(type(master)))
            print("\t- content: {}".format(master))
            print("\t- utf8 content: {}".format(master.decode('utf-8')))
