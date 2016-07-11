#!/usr/bin/env python
import subprocess as sp
import time


def main():
	try:
		cmd = 'python server.py &'.split()
		sp.Popen(cmd)
		time.sleep(.5)	
		
		cmd = 'open http://localhost:8000/proto'.split()
		sp.Popen(cmd)	#open in default browser
		
	except:
		time.sleep(.5)
		print 'Cannot start server.'
		
		
if __name__ == '__main__':
	main()

