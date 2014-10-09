#!/usr/bin/python
# -*- coding: utf-8 -*-
## \file RdList.py
## \brief List of evil domains reader

import os

class RdList:
	""" \brief Class for getting evil domain list
	"""
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
