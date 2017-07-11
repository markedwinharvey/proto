<h4>proto</h4>
<h5>a web app prototype generator</h5>

<b>proto</b> is a web app prototype generator for creating a basic html/css/javascript/jquery/python
framework for web apps, packaged with a python server set to run on localhost. 

The app generator can be run from any directory by placing a simple script in .bashrc: 

In .bashrc: 

	proto(){
		python file-path-to-proto-folder/proto_gen.py
	}


Usage (initialization):

	$ proto

	Enter prototype name: frodo
	
	### New prototype: frodo ###

	Create this prototype? (y n q): y
	

Usage (starting server):
	
	$ cd frodo/frodo
	
	$ python start.py
	
	Enter port number or hit enter for default (8000): 8003
	
	Initializing server
	
	Starting new python server on port 8003...


At this point, `localhost:8003/frodo` will open in the default browser, loading content from `frodo.html`. 	
	
`proto_gen.py` renames all files containing "proto" with the new proto name (e.g., "frodo"), as it copies each file to the new directory. 
	
`proto_gen.py` utilizes `filewalker.py` to walk proto's file hierarchy for the purpose of copying
its contents into the new app directory. 


-----


Note that this readme file is a description of the use of the "proto" framework. 
The file new_readme.md becomes the readme file of the new proto-based app. 