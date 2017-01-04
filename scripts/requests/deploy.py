import requests
import json

chaincode_id = "5036"
args = ["init", "a", "100", "b", "200"]
url = "http://127.0.0.1:7050/chaincode"

headers = {
    'content-type': "application/json",
}

# Function name would be the first arg.
payload = {
    "jsonrpc": "2.0",
    "method": "deploy",
    "params": {
        "type": 1,
        "chaincodeID":{
            "name": chaincode_id
        },
        "ctorMsg": {
            "args": args
        },
    },
    "id": 1
}

response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
print(response.text)
