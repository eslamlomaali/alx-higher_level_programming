#!/bin/bash
# Write Bash script aJSON POST request to the URL and display body of response
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
