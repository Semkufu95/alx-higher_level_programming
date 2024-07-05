#!/bin/bash
#Takes in a URL and send aDELETE  request to it
curl -X DELETE -s "$1" 
