#!/bin/bash
# A bash script that take and send request to URL
curl -s "$1" | wc -c
