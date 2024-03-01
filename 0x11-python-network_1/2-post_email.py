#!/usr/bin/python3
"""Write a Python script that takes in a URL and an email, sends POST request
to the passed URL with the email as a parameter, and displays the body of
the response (decoded in utf-8)
"""

import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    link = sys.argv[1]
    result = {"email": sys.argv[2]}
    info = urllib.parse.urlencode(result).encode("ascii")

    request = urllib.request.Request(link, info)
    with urllib.request.urlopen(request) as ans:
        print(ans.read().decode("utf-8"))
