#!/bin/bash
# test
[[ "$1" == "" ]] && { exit 10; };
# Block domain
iptables -D INPUT -p tcp -d "$1" -j DROP
iptables -D OUTPUT -p tcp -d "$1" -j DROP
echo Unblocked $1;
