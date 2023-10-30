#!/bin/sh

./prmurmurd.x64
sleep 10

./initialsetup.sh
sleep 10

./createchannel.sh
sleep 10

./startmumo.sh
sleep 10