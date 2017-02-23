import requests
import json

from config import url, chaincode_id, invoke_args


headers = {
    'content-type': "application/json",
}
payload = {
    "jsonrpc": "2.0",
    "method": "invoke",
    "params": {
        "type": 1,
        "chaincodeID":{
            "name": chaincode_id
        },
        "ctorMsg": {
            "args": invoke_args
        },
    },
    "id": 3
}

response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
print(response.text)
