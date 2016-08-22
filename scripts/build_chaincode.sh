#!/usr/bin/env bash

# This script will upload user chaincode to the peer container.
# It should be triggered at the upper directory.

set -e

if [ $# != 1 ]; then
    echo "Usage: $0 CHAINCODE_NAME"
    exit 1;
fi

# Upload chaincode to container
cpath="/opt/gopath/src/github.com/hyperledger/fabric/examples/chaincode/go/"
cname=$1
if [ -e chaincodes/${cname}.go ]; then
    docker exec vp0 mkdir -p ${cpath}${cname}
    docker cp chaincodes/${cname}.go vp0:${cpath}${cname}/
    echo "Chaincode ${cname} successfully uploaded."
else
    echo "Error: chaincodes/${cname}.go not found."
    exit 1;
fi

# Build chaincode
echo "Building chaincode ..."
docker exec vp0 bash -c "cd ${cpath}${cname};go build"
echo "Chaincode ${cname} successfully built."

# Register the chaincode with the validating peer
cid=`date +%s%N | md5sum | head -c 6`
echo "Registering chaincode using ID ${cid} ..."
docker exec vp0 bash -c "cd ${cpath}${cname};CORE_CHAINCODE_ID_NAME=${cid} CORE_PEER_ADDRESS=0.0.0.0:7051 ./${cname}"
