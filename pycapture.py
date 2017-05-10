
from __future__ import print_function
import sys, os
import argparse
import platform

from BaseRecorder import *
from LinuxRecorder import *
from WindowsRecorder import *

recorder = None

if __name__ == "__main__":

	#TODO: Add argparse

	print('Starting Capture', platform.system())

	#TODO: Add platform override argument to argparse - useful from windows with MingW terminal
	PLATFORM = platform.system()

	if PLATFORM == "Linux":
		recorder = LinuxRecorder()
		print(recorder.platform)
	elif PLATFORM == "Windows":
		recoder = WindowsRecorder()
	else:
		raise SystemError('Unsupported Platoform {}'.format(PLATFORM))
		sys.exit(-1)




