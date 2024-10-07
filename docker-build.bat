@echo off
REM
REM Windows BATCH script to build docker container
REM
@echo on
docker rmi python3-client
docker build -t python3-client .
