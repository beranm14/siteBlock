#!/usr/bin/python
# -*- coding: utf-8 -*-
## \file BlockDom.py
## \brief Blocking and command execution

import time
import os
import subprocess
import syslog

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
		self.tdl=0
		self.blocking=False
	def blAll(self):
		""" Block all
		"""
		if self.blocking == False:
			rt = subprocess.Popen(['./block.sh'])
			syslog.syslog("Blocking network access, beacause somebody called not nice webpage!")
			self.tdl = time.time()
			self.blocking = True
	def unBlAll(self):
		""" Block all
		"""
		if self.blocking == True and (self.tdl + self.time*60) < time.time():
			self.blocking = False
			rt = subprocess.Popen(['./unblock.sh'])
			syslog.syslog("Unblocking network access, timeout has been reached!")
		
