#!/usr/bin/python
# -*- coding: utf-8 -*-
## \file ReadConn.py
## \brief Read connections content

import subprocess
from Queue import Empty, Full

class ReadConn:
	def __init__(self):
		exe=["tshark","-R","tcp.port==80","-T","fields","-e","text"]
		self.p = subprocess.Popen(exe, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		self.pid = self.p.pid
	def getCt(self,qi=None,qo=None):
		if qi == None and qo == None:
			print "NONE"
			return
		while(True):
			retcode = self.p.poll()
			line = self.p.stdout.readline()
			qo.put(line)
			try:
				inp=qi.get(0)
			except Empty:
				continue
			else:
				if inp == "END":
					print("Getter ending")
					qo.put("ReadConnEND")
					return

