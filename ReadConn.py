#!/usr/bin/python
# -*- coding: utf-8 -*-
## \file ReadConn.py
## \brief Read connections content

import subprocess
from Queue import Empty, Full

class ReadConn:
	def getCt(self,qi=None,qo=None):
		exe=["tshark","-Y","tcp.port==80","-T","fields","-e","text","-W","n"]
		p = subprocess.Popen(exe, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		if qi == None and qo == None:
			print "NONE"
			return
		while(True):
			retcode = p.poll()
			line = p.stdout.readline()
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

