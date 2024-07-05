#!/bin/bash
# displays all HTTP methods the server will accept
curl -Is "$1" | sed -n '/Allow: /s/Allow: //p'
