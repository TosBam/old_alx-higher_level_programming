#!/bin/bash
# Script that sends a POST request and displays the body response with variables
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
