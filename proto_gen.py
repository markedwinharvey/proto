#!/usr/bin/env python
'''
web app prototype generator
'''
import subprocess,os,time
def main():
	filename = raw_input('Enter prototype name: ')					#get filename
	print '### New prototype:',filename,'###'
	resp = ''
	while resp not in list('ynq'):
		resp = raw_input('Create this prototype? (y n q): ')		#verify creation
	if resp in list('qn'):
		print 'Exiting...';return
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
		else:														#generate static directory
			subprocess.Popen(['mkdir '+filename+'/static'],shell=True)
			static_list = subprocess.Popen(['ls '+path+p_file],stdout=subprocess.PIPE,shell=True).communicate()[0].split()
			for static_file in static_list:
				with open(path+p_file+'/'+static_file,'r') as f:
					doc = f.read().replace('proto',filename)		#substitute new name
				static_file = filename+static_file[5:]
				with open(filename+'/'+p_file+'/'+static_file,'w') as f:
					f.write(doc)
	time.sleep(.5)
	subprocess.Popen(['chmod +x '+filename+'/*'],shell=True)		#set permissions
	subprocess.Popen(['chmod +x '+filename+'/static/*'],shell=True)
if __name__ == '__main__':
	main()