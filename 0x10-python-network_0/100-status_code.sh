#!/bin/bash
# Write script sends req URL as arg and display only status code of response
curl -s -o /dev/null -w "%{http_code}" "$1"
