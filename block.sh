#!/bin/sh
# Block all
iptables -P INPUT DROP;
iptables -P OUTPUT DROP;
iptables -P FORWARD DROP;
iptables -F;
iptables -X;

echo Blocked all;
