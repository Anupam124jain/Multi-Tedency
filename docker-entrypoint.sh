#!/bin/bash
set -e
sh -c '/home/anupam/Documents/workspace/DjangoProject/MultiTenancy/multi_tedency/wait-for-it.sh mysql:3306 -t 30'
exec "$@
