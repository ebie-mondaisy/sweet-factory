#!/bin/bash

rsync docker-compose.yaml nginx.conf swarm-manager:

ssh swarm-manager << EOF
docker stack deploy --compose-file docker-compose.yaml sweet-factory
EOF