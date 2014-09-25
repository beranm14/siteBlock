#!/usr/bin/python
# -*- coding: utf-8 -*-
## \file main.py
## \brief Louncher method

import os.path
import subprocess
from NetstPar import NetstPar
from RdList import RdList
from BlockDom import BlockDom
from WhatBlock import WhatBlock
import time

class Chdir:
	""" \brief Class for rewriting path
	"""
	def __init__( self, newPath ):
		""" Constructor of the class
		\param self Pointer on class
		\param newPath New path
		"""
		## Saved path
		self.savedPath = os.getcwd()
		os.chdir(newPath)
	def __del__( self ):
		""" Desctructor on class
		\param self Pointer on class
		"""
		os.chdir( self.savedPath)

if __name__ == "__main__":
	cd=Chdir("/opt/siteBlock/")
	# Getting what to block
	w=WhatBlock()
	# Loading nestat
	net=NetstPar()
	# loading malicious words and domains
	rd=RdList()
	ld=rd.loadLsDom()
	lw=rd.loadLsNst()
	# blocking class
	bd=BlockDom()
	
	print w.getBl()
	
	
	while 1:
		listCn=net.getList()
		dms=[]
		for i in listCn:
			if i['dns_d'].replace(" ","") == "":
				continue
			for k in ld:
				if i['dns_d'].find(k) != -1 :
					if w.getBl() == "domains":
						bd.blDom(i['dns_d'])
					elif w.getBl() == "all":
						bd.blAll(i['dns_d'])
			if i['dns_d']:
				dms.append(i['dns_d'])
		for i in lw:
			for j in dms:
				if j.find(i) != -1:
					if w.getBl() == "domains":
						bd.blDom(j)
					elif w.getBl() == "all":
						bd.blAll(j)
		if w.getBl() == "domains":
			bd.unBlDom()
		elif w.getBl() == "all":
			bd.unBlAll()
			
		
		time.sleep(4)