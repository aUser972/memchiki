#!/bin/bash
JSON=$(cat request.json)
curl -X GET -H "Content-Type: application/json" -d"$JSON" http://127.0.0.1:8000
