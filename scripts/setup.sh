#!/usr/bin/env bash

# This script will check the env and (re)start all services.
# It should be triggered by root, and safe to repeat.

apt-get update
apt-get install -y curl python-pip

echo "Checking Docker-engine..."
command -v docker >/dev/null 2>&1 || { echo >&2 "No docker-engine found, try installing"; curl -sSL https://get.docker.com/ | sh; service docker restart; }

echo "Checking Docker-compose..."
command -v docker-compose >/dev/null 2>&1 || { echo >&2 "No docker-compose found, try installing"; pip install docker-compose; }

echo "Checking local Docker image..."
[[ "$(docker images -q hyperledger/fabric-peer:x86_64-0.6.1-preview 2> /dev/null)" == "" ]] && echo "hyperledger/fabric-peer:x86_64-0.6.1-preview is not there, may use some time to pull it down for the first time running" && docker pull hyperledger/fabric-peer:x86_64-0.6.1-preview && docker tag hyperledger/fabric-peer:x86_64-0.6.1-preview hyperledger/fabric-peer:latest
[[ "$(docker images -q hyperledger/fabric-membersrvc:x86_64-0.6.1-preview 2> /dev/null)" == "" ]] && echo "hyperledger/fabric-membersrvc:x86_64-0.6.1-preview is not there, may use some time to pull it down for the first time running" && docker pull hyperledger/fabric-membersrvc:x86_64-0.6.1-preview && docker tag hyperledger/fabric-membersrvc:x86_64-0.6.1-preview hyperledger/fabric-membersrvc:latest
