#!/usr/bin/python
# -*- coding: utf-8 -*-
## \file BlockDom.py
## \brief Blocking and command execution

import time
import os
import subprocess
import syslog
import socket

class BlockDom:
	""" \brief Class for blocking domain
	"""
	def __init__(self,time="10",pth="./delay.txt"):
		""" Constructor loading time delay between blockings
		"""
		## Time delay for blocking
		self.time=time
		if os.path.isfile(pth):
			f=open(pth,"r")
			cn=f.read()
			tm=cn.split("\n")[0].replace(" ","")
			if tm.isdigit():
				self.time=int(tm)
			f.close()
		self.blocks=[]
	def blAll(self,name):
		""" Block all
		"""
		for j in self.blocks:
			if j['name'] == name:
				return
		i={}
		i['name']=name
		i['time']=time.time()
		try:
			ip = socket.gethostbyname(name)
		except:
			return
		i['ip']=ip		
		print "Blocking all"
		self.blocks.append(i)
		rt = subprocess.Popen(['./block.sh'])
		syslog.syslog("Blocking network access, beacause somebody called not nice webpage!")
	def unBlAll(self):
		""" Block all
		"""
		for i in self.blocks:
			if i['time'] + self.time*60 < time.time():
				print "Unblocking all"
				self.blocks.remove(i)
				rt = subprocess.Popen(['./unblock.sh'])
				syslog.syslog("Unblocking network access, timeout has been reached!")
				break
	def blDom(self,name):
		""" Block domain
		"""
		for j in self.blocks:
			if j['name'] == name:
				return
		i={}
		i['name']=name
		i['time']=time.time()
		try:
			ip = socket.gethostbyname(name)
		except:
			return
		i['ip']=ip		
		print "Blocking " + i['name']
		rt = subprocess.Popen(['./blockdom.sh',i['name']])
		self.blocks.append(i)
		syslog.syslog("Blocking " + i['name'] + ", domain contain nasty words or is on list of malicious domains!")
	def unBlDom(self):
		""" Unblock domain
		"""
		for i in self.blocks:
			if i['time'] + self.time*60 < time.time():
				print "Unblocking " + i['name']
				rt = subprocess.Popen(['./unblockdom.sh',i['ip']])
				self.blocks.remove(i)
				syslog.syslog("Unblocking " + i['name'] + ", beware the domain could be still on the list!")
				break
		
#b=BlockDom()
#print b.time