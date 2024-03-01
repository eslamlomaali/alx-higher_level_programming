#!/usr/bin/python3
"""Write a Python script that takes in a URL, sends a request to the URL
and displays the body of the response.
"""
import sys
import requests


if __name__ == "__main__":
    link = sys.argv[1]

    res = requests.get(link)
    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
    else:
        print(res.text)
