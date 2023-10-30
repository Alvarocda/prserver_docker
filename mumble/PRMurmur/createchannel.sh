#!/bin/sh
cd mumo/tools
IFS=""

#echo -n "Name of Channel (i.e. Awesome PR Server): "
#read CHANNEL_NAME
#echo -n "Unique Channel ID (i.e. awesome): "
#read CHANNEL_ID
#echo -n "Server IP (i.e. 123.123.123.123): "
#read IP
#echo -n "Server Game Port (i.e. 16567): "
#read PORT

python prbf2man.py -c $CHANNEL_ID -n $CHANNEL_NAME -f $IP:$PORT -b 1 -o "../modules-enabled/prbf2.ini" -s prmurmurpassword -i "../../PRMurmur.ice" 
