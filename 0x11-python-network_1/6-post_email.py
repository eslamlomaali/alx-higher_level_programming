#!/usr/bin/python3
"""Write a Python script that takes in a URL and an email address, sends POST
request to the passed URL with the email as a parameter, and finally displays
the body of the response.
"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as ans:
        print(dict(ans.headers).get("X-Request-Id"))
