#!/bin/bash

docker-compose up -d && docker-compose scale crawler=3

docker-compose logs -f
