#!/bin/bash

URL=`terraform output -raw invoke_url`
echo "Get IP url: $URL"
echo""
curl -X GET $URL
