#!/bin/bash
# I can pass params with curl
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
