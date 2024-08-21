#!/usr/bin/python3
# A script that takes and sends request to the URL and displays value ID

from urllib import request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    with request.urlopen(url) as response:
        print(dict(response.headers).get("X-Request-Id"))
