#!/usr/bin/python3
"""fethes some ressources on the internet"""
import urllib.request
if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        res = res.read()
        print(f"Body response")
        print(f"\t- type: {type(res)}")
        print(f"\t- content: {res}")
        print(f"\t- utf8 content: {res.decode(encoding='utf8')}")
