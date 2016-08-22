import requests
import json
import base64

chaincode_id = "3112a6"
args = ["invoke", "a", "b", "5"]
url = "http://127.0.0.1:7050/chaincode"

headers = {
    'content-type': "application/json",
}

# For current fabric version, args need to be base64 encoded.
# Function name would be the first arg.
args_b64 = [base64.b64encode(i) for i in args]
payload = {
    "jsonrpc": "2.0",
    "method": "invoke",
    "params": {
        "type": 1,
        "chaincodeID":{
            "name": chaincode_id
        },
        "ctorMsg": {
            "args": args_b64
        },
    },
    "id": 3
}

response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
print(response.text)