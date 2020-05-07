#!/bin/bash

docker-compose up -d && docker-compose scale crawler=4

docker-compose logs -f
