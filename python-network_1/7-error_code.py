#!/usr/bin/python3
"""Displays the body of a response, or the error code if >= 400"""
import requests
import sys

response = requests.get(sys.argv[1])
if response.status_code >= 400:
    print("Error code: {}".format(response.status_code))
else:
    print(response.text)
