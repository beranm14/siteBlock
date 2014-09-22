#!/usr/bin/python
# -*- coding: utf-8 -*-
## \file NetstPar.py
## \brief Netstat parsing

import socket
import os

class NetstPar:
	""" \brief Class for getting stats from /proc/net/(udp,tcp) 
	"""
	def __init__(self,tcpp="/proc/net/tcp",udpp="/proc/net/udp"):
		""" Constructor
		\param tcpp Path to tcp connection table
		\param udpp Path to udp connection table
		"""
		if os.path.isfile(tcpp):
			## tcp connection table
			self.tcp=tcpp
		else:
			raise FileNotFoundError("TCP table file not found")
		if os.path.isfile(udpp):
			## udp connection table
			self.udp=udpp
		else:
			raise FileNotFoundError("UDP table file not found")
	def getList(self):
		""" Gether for tcp/udp connections
		\return List of source Ip, destionation Ip, uid of owner, destination dns name
		"""
		cn=""
		
		f=open(self.tcp,"r")
		tm=f.read()
		tm=tm.split("\n")[1:]
		for i in tm:
			cn +=  i  + "\n" 
		f.close()
		
		f=open(self.udp,"r")
		tm=f.read()
		tm=tm.split("\n")[1:]
		for i in tm:
			cn +=  i  + "\n" 
		f.close()
		
		ret=[]
		for ln in cn.split("\n"):
			if ln.replace(" ","") != "":
				f=ln.split()
				t=dict()
				
				t['uid']=f[7]
				t['unm']=self.getUidNm(f[7])
				
				
				t['ip_s'] = self.hexdec(f[1].split(":")[0][6:8])
				t['ip_s'] += "." + self.hexdec(str(f[1].split(":")[0][4:6]))
				t['ip_s'] += "." + self.hexdec(str(f[1].split(":")[0][2:4]))
				t['ip_s'] += "." + self.hexdec(str(f[1].split(":")[0][0:2]))
				t['port_s'] = self.hexdec(f[1].split(":")[1])
				
				t['ip_d'] = self.hexdec(f[2].split(":")[0][6:8])
				t['ip_d'] += "." + self.hexdec(str(f[2].split(":")[0][4:6]))
				t['ip_d'] += "." + self.hexdec(str(f[2].split(":")[0][2:4]))
				t['ip_d'] += "." + self.hexdec(str(f[2].split(":")[0][0:2]))
				t['port_d'] = self.hexdec(f[2].split(":")[1])

				t['dns_d'] = self.getIpNm(t['ip_d'])
				ret.append(t)
		return ret
	def getUidNm(self,uid):
		""" Get name from uid
		\param uid of user
		"""
		f=open("/etc/passwd","r")
		co=f.readlines()
		f.close()
		for i in co:
			if uid == i.split(":")[2]:
				return i.split(":")[0]
	def getIpNm(self,ip):
		""" IP to dname
		\param Ip adress to resolve
		"""
		t=""
		try:
			res = socket.gethostbyaddr(ip)
			t=res[0]
		except:
			t=""
		return t
	def hexdec(self,hex):
		""" Hex to dec
		\param hex number
		"""
		return str(int(hex,16))
		
n=NetstPar()
print n.getList()