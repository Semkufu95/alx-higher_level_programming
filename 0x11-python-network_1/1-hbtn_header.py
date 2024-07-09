#!/usr/bin/python3
# A script that takes and sends request to the URL and displays value ID

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        headers = response.getheaders()
        for header in headers:
            if header[0].lower() == "x-request-id":
                print(header[1])
                break
