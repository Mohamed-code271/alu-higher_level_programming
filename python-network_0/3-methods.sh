#!/bin/bash
# Displays all HTTP methods the server accepts
curl -s -X OPTIONS -i "$1" | grep -i "^allow:" | cut -d' ' -f2- | tr -d '\r'
