#!/bin/bash
# Write Bash script that takes in URL sends request for URL, and displays size
curl -s "$1" | wc -c
