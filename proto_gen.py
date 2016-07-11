#!/usr/bin/env python
'''
web app prototype generator
prompts for app name; copies and renames all files from proto folder
'''
import subprocess as sp
import filewalker as fw
import sys
import os

def get_proto_name():
	filename = raw_input('Enter prototype name: ')					#get filename
	print '### New prototype:',filename,'###'
	resp = ''
	while resp not in list('ynq'):
		resp = raw_input('Create this prototype? (y n q): ')		#verify action
	if resp in list('qn'):
		print 'Exiting...'
		sys.exit()
	return filename


def main():
	
	filename = get_proto_name()
	sp.Popen(['mkdir',filename])
	
	#--------walk the proto hierarchy--------#
	root = os.path.dirname(__file__)
	files,dirs,ftree = fw.walk(root=root)
	
	for dir in dirs:	#create all directories first
		rel_path = dir.rel.replace('proto',filename)
		sp.Popen(['mkdir',filename+'/'+rel_path])
	
	#--------do not comment in files_to_modify--------#
	#The contents of the following files will be modified (other files will be modified in name only)
	files_to_modify = [x for x in '''
		
		proto
		proto.html
		setup.py
		start.py
		
	'''.replace('\t','').split('\n') if x]
	#--------do not comment in files_to_modify--------#
	
	for file in files:
		if file.name in ['proto_gen.py','readme.md']:
			continue
		
		rel_path = file.rel.replace('proto',filename)
		with open(file.abs,'r') as f:
			doc = f.read()
		if file.name in files_to_modify:
			doc = doc.replace('proto',filename)
		with open(filename+'/'+rel_path,'w') as f:
			f.write(doc)
			
		cmd = str('chmod +x '+filename+'/'+rel_path).split()
		sp.Popen(cmd)
		sp.Popen(['touch',filename+'/'+'readme.md'])

if __name__ == '__main__':
	main()