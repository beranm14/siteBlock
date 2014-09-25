#!/bin/bash
# test
[[ "$1" == "" ]] && exit 10;
# Block domain
iptables -I INPUT -p tcp -d "$1" -j DROP
iptables -I OUTPUT -p tcp -d "$1" -j DROP
echo Blocked $1;
