COMPOSE_FILE="docker-compose-2orgs-4peers.yaml"

all:
	make start
	sleep 3
	make test
	sleep 3
	make stop

setup: # setup the environment
	bash scripts/setup_Docker.sh  # Install Docker, Docker-Compose
	bash scripts/download_images.sh  # Pull required Docker images

start: # bootup the fabric network
	docker-compose -f ${COMPOSE_FILE} up -d  # Start a fabric network with mvp

test: # test chaincode
	docker exec -it fabric-cli bash ./scripts/test_1peer.sh

stop: # stop the fabric network
	docker-compose -f ${COMPOSE_FILE} down  # Stop a fabric network
