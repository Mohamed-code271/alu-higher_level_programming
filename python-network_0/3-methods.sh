#!/bin/bash
curl -s -X OPTIONS -I "$1" | grep -i "allow:" | sed 's/[Aa]llow: //' | tr -d '\r'
