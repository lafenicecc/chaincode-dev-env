#!/usr/bin/env bash

# This script will check the env and (re)start all services.
# It should be triggered at the upper directory, and safe to repeat.

sudo apt-get install -y curl docker-engine python-pip

echo "Checking Docker-engine..."
command -v docker >/dev/null 2>&1 || { echo >&2 "No docker-engine found, try installing"; curl -sSL https://get.docker.com/ | sh; sudo service docker restart; exit 0; }

echo "Checking Docker-compose..."
command -v docker-compose >/dev/null 2>&1 || { echo >&2 "No docker-compose found, try installing"; sudo pip install -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com docker-compose; exit 0; }

echo "Checking local Docker image..."
[[ "$(docker images -q hyperledger/fabric-peer:latest 2> /dev/null)" == "" ]] && echo "hyperledger/fabric-peer:latest is not there, may use some time to pull it down for the first time running" && docker pull hyperledger/fabric-peer
[[ "$(docker images -q hyperledger/fabric-membersrvc:latest 2> /dev/null)" == "" ]] && echo "hyperledger/fabric-membersrvc:latest is not there, may use some time to pull it down for the first time running" && docker pull hyperledger/fabric-membersrvc

echo "Stop all services..."
docker-compose stop

echo "Remove all services..."
docker-compose rm -f -all

echo "Restart all services..."
docker-compose up -d --no-recreate
