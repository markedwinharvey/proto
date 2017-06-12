#!/usr/bin/env python
import subprocess as sp
import time
import requests
import kill_server
import sys

def check_localhost( port ):
	'''404 message implies a server at port 8000 is running with a root directory elsewhere'''
	'''if so, kill it'''
	r = requests.get('http://127.0.0.1:%s/proto' % port)
	if r.status_code == 404:
		print 'Got 404 message; attempting server kill'
		
		kill_server.main()
	else:
		print 'Returned status code:',r.status_code
		if r.status_code == 200:
			print 'Opening page...'
			#status ok; server running from current directory; open page
			cmd = ('open http://localhost:%s/proto' % port).split()
			sp.Popen(cmd)	#open in default browser
			return
			
	start()

def start( port ):
	#port = 8000
	try:
		print 'Starting new python server on port %s' % port
		cmd = 'python server.py &'.split()
		sp.Popen(cmd)
		time.sleep(.5)	
		
		cmd = ('open http://localhost:8000/%s' % port).split()
		sp.Popen(cmd)	#open in default browser
		
	except:
		time.sleep(.5)
		print 'Cannot start server.'
		
		
def main():
	print 'Initiating server'
	port = raw_input('Enter port number or hit enter for default (8000): ')
	if not port: port = 8000
	
	try:
		check_localhost( port )
		
	except:
		'''no connection to localhost found; start server'''
		start( port )

	
		
if __name__ == '__main__':
	main()

