#!/usr/bin/python
# -*- coding: utf-8 -*-
## \file WhatBlock.py
## \brief Conf file loader on what to block

import os

class WhatBlock:
	""" \brief Conf file loader on what to block
	"""
	def __init__(self,time="10",pth="./whatblock.txt"):
		""" Constructor loading time delay between blockings
		"""
		## Path to conf file
		self.pth=pth
		## What to block
		self.bl="All"
		if os.path.isfile(pth) == False:
			self.bl="All"
		else:
			self.setBl()
	def setBl(self):
		""" Setter on bl
		"""
		f=open(self.pth,"r")
		cn=f.read()
		f.close()
		for i in cn.split("\n"):
			wh = i.find("#")
			if wh != -1:
				str = i[0:wh]
			else:
				str = i
			if str.replace(" ","") == "domains":
				self.bl="domains"
			elif str.replace(" ","") == "all":
				self.bl="all"
	def getBl(self):
		""" Getter on what to block
		"""
		return self.bl
