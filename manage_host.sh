#! /bin/bash

# For Activating the Client
Activate(){
   sudo sed -i "2i127.0.0.1 $1"  /etc/hosts
}

# For Deactivating the Client
Deactivate(){
   sudo sed -i".bak" "/$1/d" /etc/hosts
}

# Conditionally Invoke the functions

if [ $1 == 'activate' ]
then
   Activate $2
elif [ $1 == 'deactivate' ]
then
   Deactivate $2
else
   echo "Do Nothing"
fi

