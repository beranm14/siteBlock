#!/usr/bin/python
# -*- coding: utf-8 -*-
## \file RdList.py
## \brief List of evil domains reader

import socket
import os
import urllib2

class RdList:
	""" \brief Class for getting evil domain list
	"""
	def __init__(self,pth="./list.txt"):
		""" Constructoe
		\param pth Path to list
		"""
		## Path to list of malicious domains
		self.pth=pth
	def getUpLs(self):
		""" Method for updating the list
		"""
		res= urllib2.urlopen('http://www.malwaredomainlist.com/mdlcsv.php')
		cn = res.read().split("\n")
		tod=""
		try:
			orig=open(self.pth,"r").readlines()
		except:
			orig=""
		for i in cn:
			if i == "" or i.split(",")[1].replace("\"","") == "-":
				continue
			ts = i.split(",")[1].replace("\"","")
			if ts not in orig:
				tod += i.split(",")[1].replace("\"","") + "\n"
		f=open(self.pth,"a")
		f.write(tod)
		f.close()
		
r=RdList()
r.getUpLs()