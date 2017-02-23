import requests
import json

from config import url, chaincode_id, query_args


headers = {
    'content-type': "application/json",
}
payload = {
    "jsonrpc": "2.0",
    "method": "query",
    "params": {
        "type": 1,
        "chaincodeID":{
            "name": chaincode_id
        },
        "ctorMsg": {
            "args": query_args
        },
    },
    "id": 5
}

response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
print(response.text)
