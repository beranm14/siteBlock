#!/usr/bin/python
# -*- coding: utf-8 -*-
## \file main.py
## \brief Louncher of app

import signal
import os.path
import subprocess

def signalHandler(signal, frame):
	print("Ending")

class Chdir:
	def __init__( self, newPath ):
		self.savedPath = os.getcwd()
		os.chdir(newPath)
	def __del__( self ):
		os.chdir( self.savedPath)

if __name__ == "__main__":
	signal.signal(signal.SIGINT, signalHandler)
	signal.signal(signal.SIGQUIT, signalHandler)
	cd=Chdir("/usr/share/contBlock")
	bc=subprocess.call("./contBlock", shell=True)
	exit(bc)
