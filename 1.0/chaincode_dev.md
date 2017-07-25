## Chaincode development environment

### Setup host environment

Install docker and docker-compose.

```sh
bash scripts/setup_Docker.sh
```

Download necessary docker images.

```sh
bash scripts/download_images.sh
```

### Start a fabric network

Start a minimal fabric network for chaincode dev. The network includes 1 peer, 1 orderer, 1 ca and 1 cli.

```sh
bash scripts/start_fabric_ccdev.sh
```

The cli contains a Restful server, listening on port 8080.

### Setup channel

Use following request to create a channel "businesschannel".

```
GET /api/create_channel
```

Use following request to make the peer join the channel.

```
GET /api/join_channel
```

Use following request to update anchor peer.

```
GET /api/update_anchor_peers
```

Now we have a channel, ready to install and test chaincodes.

### Install and test chaincodes

Put the chaincode folder inside `1.0/mychaincodes/`.

Install a new chaincode (or install a new version of chaincode before upgrade). For example,

```
POST /api/install_chaincode
{
    "name": "mycc",
    "version": "1.0",
    "path": "github.com/hyperledger/fabric/mychaincodes/<folder_name>"
}
```

Instantiate (or upgrade) the chaincode.

```
POST /api/instantiate_chaincode
{
    "name": "mycc",
    "version": "1.0",
    "ctor": "{\"Args\":[\"init\",\"a\",\"100\",\"b\",\"200\"]}"
}
```

```
POST /api/upgrade_chaincode
{
    "name": "mycc",
    "version": "1.1",
    "ctor": "{\"Args\": [\"re-init\",\"c\",\"500\"]}"
}
```

If successful, you should see the chaincode docker container running. Can use `docker logs -f <container_name>` to monitor the container logs.

Invoke the chaincode.

```
POST /api/invoke_chaincode
{
    "name": "mycc",
    "ctor": "{\"Args\": [\"move\",\"a\",\"b\",\"10\"]}"
}
```

Query the chaincode.

```
POST /api/query_chaincode
{
    "name": "mycc",
    "ctor": "{\"Args\": [\"query",\"a\"]}"
}
```
