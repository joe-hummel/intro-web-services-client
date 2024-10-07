#!/bin/bash
#
# Linux/Mac BASH script to build docker container
#
docker rmi python3-client
docker build -t python3-client .
