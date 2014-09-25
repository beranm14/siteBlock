#!/bin/sh
# Unblock all
iptables -F;
iptables -X;
iptables -A OUTPUT -j ACCEPT;
iptables -A INPUT -j ACCEPT;
echo Unblocked all;
