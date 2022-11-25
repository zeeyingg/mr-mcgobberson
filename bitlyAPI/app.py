# from flask import Flask, render_template
import requests, json

headers = {
  'Authorization': 'Bearer 171ba25afaef729e412ddb560e7881b08d7e1dfb',
  'Content-Type': 'application/json',
}

data = '{ "long_url": "https://dev.bitly.com", "domain": "bit.ly", "group_guid": "Ba1bc23dE4F" }'

response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, data=data)

message = (json.load(open(response)))
print(message)
  
