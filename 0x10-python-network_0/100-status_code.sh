#!/bin/bash
# Bash script that sends a request to a URL passed as an argument and display status code
awk 'NR==1{printf "%s", $2}' test7 $(curl -sI "$1" -o test7)
