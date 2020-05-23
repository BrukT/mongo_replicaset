#!/bin/bash

echo ***************************************
echo Starting the replica set
echo ***************************************

sleep 10 | echo Sleeping
mongo mongodb://mongo1:27017 replicaSet.js
#sleep 20 | echo Sleeping
#python testScript.py