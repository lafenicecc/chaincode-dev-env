#!/usr/bin/env bash

# This script will upload user chaincode to the peer container.
# It should be triggered at the upper directory.

if [ $# != 1 ]; then
    echo "USAGE: $0 CHAINCODE_NAME"
    echo "e.g.: $0 MyChaincode"
    exit 1;
fi

name=$1
if [ -e chaincodes/${name}.go ]; then
    docker exec vp0 mkdir -p /opt/gopath/src/github.com/hyperledger/fabric/examples/chaincode/go/${name}
    docker cp chaincodes/${name}.go vp0:/opt/gopath/src/github.com/hyperledger/fabric/examples/chaincode/go/${name}/
    echo "Chaincode ${name} successfully uploaded"
else
    echo "chaincodes/${name}.go not found"
    exit 1;
fi

