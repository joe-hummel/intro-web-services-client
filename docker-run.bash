#!/bin/bash
#
# Linux/Mac BASH script to run docker container
#
docker run -it -u user -w /home/user -v .:/home/user --network="host" --rm python3-client bash
