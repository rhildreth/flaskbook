from flask import Flask, request, jsonify
import json,httplib
connection = httplib.HTTPSConnection('parseapi.back4app.com', 443)
connection.connect()
connection.request('POST', '/classes/Charges', json.dumps({
       "score": 1337,
       "playerName": "Sean Plott",
       "cheatMode": False
     }), {
       "X-Parse-Application-Id": "D6BrpJcyNiZWmGSozfOeizhcASzHDjNeMeqYbSb2",
       "X-Parse-REST-API-Key": "YRRgxBWf1lhkLhpnNQsvCIFHLny44HWsOIdsq3rN",
       "Content-Type": "application/json"
     })
results = connection.getresponse().read()
print results