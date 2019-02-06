#!/bin/bash

# Functions
ok() { echo -e '\e[32m'$1'\e[m'; } # Green

EXPECTED_ARGS=3
E_BADARGS=65     #Wrong number of argument pass in a script
MYSQL=`which mysql`
 
Q1="CREATE DATABASE IF NOT EXISTS $1;"
Q2="GRANT ALL ON *.* TO '$2'@'localhost' IDENTIFIED BY '$3';"
Q3="FLUSH PRIVILEGES;"
SQL="${Q1}${Q2}${Q3}"
 
if [ $# -ne $EXPECTED_ARGS ]
then
  echo "Usage: $0 dbname dbuser dbpass"
  exit $E_BADARGS
fi

/opt/lampp/bin/mysql -u root -p -e "$SQL"

ok "Database $1 and user $2 created with a password $3"

source "/home/anupam/Documents/envs/multi_tenents/bin/activate"
python /home/anupam/Documents/workspace/DjangoProject/multi_tedency/manage.py migrate --database=$1
deactivate