#!/usr/bin/python3
"""
    script that takes in a URL and an email,
    sends a POST request to the passed URL with the email as a parameter,
    and displays the body of the response (decoded in utf-8)
"""

import sys
from urllib import request
from urllib import parse

if __name__ == "__main__":
    # Get the URL and email from the command line argument
    url = sys.argv[1]
    email = sys.argv[2]

    # Create a dictionary with the email parameter
    data = {'email': email}

    # Encode the data to be sent in the request body
    encoded_data = parse.urlencode(data).encode('ascii')

    # Make a POST request to the provided URL with the email parameter
    with request.urlopen(url, data=encoded_data) as response:
        # read and decode the response body in utf-8
        print(response.read().decode('utf-8'))
