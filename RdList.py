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
	def getUpLs(self,csvDwn='http://www.malwaredomainlist.com/mdlcsv.php'):
		""" Method for updating the list
		"""
		j=0
		try:
			res= urllib2.urlopen(csvDwn)
		except urllib2.URLError:
			print "Unable to connect to " + csvDwn
			return
		
		#res= urllib2.urlopen(csvDwn)
		cn = res.read().split("\n")
		tod=""
		try:
			r=open(self.pth,"r").read()
			orig=[]
			for i in r.split("\n"):
				orig.append(i)
		except:
			orig=[]
		add=[]
		for i in cn:
			if i == "" or i.split(",")[1].replace("\"","") == "-":
				continue
			ts = i.split(",")[1].replace("\"","")
			ts = ts[0:ts.find("/")]
			if ts not in orig and ts not in add:
				add.append(ts)
				tod += ts + "\n"
				j += 1
		f=open(self.pth,"a")
		f.write(tod)
		f.close()
		print str(j) + " added"
	def getUpLh(self,csvDwn='http://winhelp2002.mvps.org/hosts.txt'):
		""" Method for updating the list
		"""
		j=0
		try:
			res= urllib2.urlopen(csvDwn)
		except urllib2.URLError:
			print "Unable to connect to " + csvDwn
			return
		cn = res.read().split("\n")
		tod=""
		try:
			r=open(self.pth,"r").read()
			orig=[]
			for i in r.split("\n"):
				orig.append(i)
		except:
			orig=[]
		add=[]
		for i in cn:
			if i == "" or i[0] == "#":
				continue
			ks = i.split()
			if len(ks) < 2:
				continue
			ts=ks[1]
			if ts not in orig and ts not in add:
				add.append(ts)
				tod += ts + "\n"
				j += 1
		f=open(self.pth,"a")
		f.write(tod)
		f.close()
		print str(j) + " added"
	def loadLsNst(self,pth="./nasty_wrds.txt"):
		""" Method for loading nasty words from nasty_wrds.txt
		"""
		ret = []
		if os.path.isfile(pth) == False:
			return ret
		f=open(pth,"r")
		cn=f.read()
		f.close()
		for i in cn.split("\n"):
			if i.replace(" ","") != "":
				ret.append(i)
		return ret
	def loadLsDom(self,pth="./list.txt"):
		""" Method for loading nasty domains from list.txt
		"""
		ret = []
		if os.path.isfile(pth) == False:
			return ret
		self.pth=pth
		f=open(pth,"r")
		cn=f.read()
		f.close()
		for i in cn.split("\n"):
			if i.replace(" ","") != "":
				ret.append(i)
		return ret
if __name__ == "__main__":
	r=RdList()
	r.getUpLh()
	r.getUpLs()