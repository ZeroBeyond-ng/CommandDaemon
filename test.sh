#!/bin/bash
# A simple script that executes a simple Web request 
# using curl.
#
# curl --header "Content-Type: application/json" \
  # --request POST \
  # --data '{"username":"xyz","password":"xyz"}' \
  # http://localhost:3000/api/login
curl -X POST -F  "command=exec" http://127.0.0.1:17777
