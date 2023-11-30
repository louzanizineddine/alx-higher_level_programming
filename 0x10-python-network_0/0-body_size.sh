#!/bin/bash
#display body size
curl -s "$1" | wc -c
