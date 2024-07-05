#!/bin/bash
# Takes in URL, sends request to the URL and display size of the body of response
curl -sw "%{size_download}\n" -o /dev/null '$1'
