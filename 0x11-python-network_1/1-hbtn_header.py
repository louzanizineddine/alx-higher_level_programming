#!/usr/bin/python3
"""fethes some ressources on the internet"""
import urllib.request
import sys
if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as res:
        print(dict(res.headers).get("X-Request-Id"))
