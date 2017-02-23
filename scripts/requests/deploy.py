import requests
import json

from config import url, chaincode_id, deploy_args


headers = {
    'content-type': "application/json",
}
payload = {
    "jsonrpc": "2.0",
    "method": "deploy",
    "params": {
        "type": 1,
        "chaincodeID":{
            "name": chaincode_id
        },
        "ctorMsg": {
            "args": deploy_args
        },
    },
    "id": 1
}

response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
print(response.text)
