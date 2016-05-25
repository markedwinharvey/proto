#!/usr/bin/env python
'''
web app prototype generator
prompts for app name; copies and renames all files from proto folder
'''
import subprocess,os,time

def main():
	#----------start program; get filename------------#
	filename = raw_input('Enter prototype name: ')					#get filename
	print '### New prototype:',filename,'###'
	resp = ''
	while resp not in list('ynq'):
		resp = raw_input('Create this prototype? (y n q): ')		#verify creation
	if resp in list('qn'):
		print 'Exiting...';return
	
	#-----------create directory/files/subfolders---------#
	subprocess.Popen(['mkdir '+filename],shell=True)				#create directory
	home_dir = os.path.expanduser('~')
	path = home_dir+'/p/proto/proto/'	
	file_list = subprocess.Popen(['ls '+path],stdout=subprocess.PIPE,shell=True).communicate()[0].split()	#get proto file_list
	for p_file in file_list:
		if not os.path.isdir(path+p_file):
			with open(path+p_file,'r') as f:
				doc = f.read().replace('proto',filename)			#open proto file and substitute new name
			if p_file[:5] == 'proto':
				p_file = filename+p_file[5:]
			with open(filename+'/'+p_file,'w') as f:
				f.write(doc)
		#--------------generate subfolders/contents--------------#
		else:	
			subprocess.Popen(['mkdir '+filename+'/'+p_file],shell=True)
			files_in_subfolder = subprocess.Popen(['ls '+path+p_file],stdout=subprocess.PIPE,shell=True).communicate()[0].split()
			for each_file in files_in_subfolder:
				with open(path+p_file+'/'+each_file,'r') as f:
					doc = f.read()
				if each_file[:6] != 'jquery' and each_file[:7] != 'angular':
					doc=doc.replace('proto',filename)				#replace internal 'proto'
				each_file = each_file.replace('proto',filename)		#replace filename 'proto'
				with open(filename+'/'+p_file+'/'+each_file,'w') as f:
					f.write(doc)
		
	time.sleep(.5)
	subprocess.Popen(['chmod +x '+filename+'/*'],shell=True)		#set permissions
	subprocess.Popen(['chmod +x '+filename+'/static/*'],shell=True)
if __name__ == '__main__':
	main()