echo "Stop all services..."
docker-compose stop

echo "Remove all services..."
docker-compose rm -f -all

echo "Restart all services..."
docker-compose up -d --no-recreate

