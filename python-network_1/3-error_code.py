#!/usr/bin/python3
"""Displays the body of a response, or the HTTP error code on failure"""
import urllib.request
import urllib.error
import sys

try:
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.read().decode('utf-8'))
except urllib.error.HTTPError as e:
    print("Error code: {}".format(e.code))
