#!/bin/bash
# script takes in URL sends POST request to URL and displays body of response
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
