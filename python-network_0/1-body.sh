#!/bin/bash
curl -s -o /tmp/body_output -w "%{http_code}" "$1" > /tmp/status_code
if [ "$(cat /tmp/status_code)" -eq 200 ]; then
    cat /tmp/body_output
fi
