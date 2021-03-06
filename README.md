![Heiko](./bot/bot_icon.png?raw=true)

# Swagger generated server

## Overview

This server was generated by the [swagger-codegen](https://github.com/swagger-api/swagger-codegen) project.

This server uses the [Connexion](https://github.com/zalando/connexion) library on top of Flask.

## Requirements

Python 3.5.2+

## Usage

To run the server locally, please execute the following from the root directory:

```
pip3 install -r requirements.txt
BLAZEGRAPHURL=$blazegraph_endpoint LOGINNAME=$username PASSWORD=$password REQUESTURL=$train_request_endpoint TOKEN=$slack_token
HOST=$host_url
python3 -m swagger_server
```

BLAZEGRAPHURL: Endpoint of the blazegraph database (required)
LOGINNAME: User name for the train request endpoint (optional, for train requests)
PASSWORD: Password for the train request endpoint (optional, for train requests)
REQUESTURL: Request endpoint (optional, for train requests)
TOKEN: Slack token (optional, for user notifications)
HOST: The base address of your host (optional, for serving images)
E.g:

```
BLAZEGRAPHURL=http://blazegraph.ba-kunz:9999/bigdata/sparql
LOGINNAME=testname
PASSWORD=testpasswort
REQUESTURL=https://padme-analytics.de
TOKEN=xoxb-etc-bla-bla
HOST=https://milki-psy.dbis.rwth-aachen.de
```

The Swagger definition lives here:

```
http://localhost:8081/api/swagger.json
```

## Running with Docker

To run the server on a Docker container, please execute the following from the root directory:

```bash
# building the image
docker build -t swagger_server .

# starting up a container
docker run -p 8081:8081 -e BLAZEGRAPHURL=$blazegraph_endpoint -e LOGINNAME=$username -e PASSWORD=$password -e REQUESTURL=$train_request_endpoint swagger_server
```

# Usage as a Bot

Please note, that this server requires -- as is -- the SBF and Blazegraph to run.
Test data for the Blazegraph database and training data for the Rasa NLU can be found in the directory /bot.
The final bot model can be found there, too.
