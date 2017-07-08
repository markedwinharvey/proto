#!/usr/bin/env python
'''
Receive json-encoded post requests from function 'post_data()' in static/proto.js
'''
import cgi
import json

print

def test(data):
	with open('TEST','w') as f:
		f.write(data)

def main():
	data = json.loads(cgi.FieldStorage()['package'].value)
	
	test('Running proto.py with the following data: %s' % data)
	
	
	result = data
	
	print json.dumps( result )
	
if __name__ == '__main__':
	main()