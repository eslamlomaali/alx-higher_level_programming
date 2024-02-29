#!/bin/bash
# Write script that takes URL and displays all methods the server will accept.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
