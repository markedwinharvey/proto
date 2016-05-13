<h4>proto</h4>
<h5>a web app prototype generator</h5>
`proto` is a web app prototype generator for creating a basic html/css/javascript/jquery/python
framework for web apps, packaged with a python server set to run on localhost. 

The generator can be run from any directory by placing a simple script in the .bashrc folder: <br>
	`proto(){
		python file-path-to-proto-folder/proto_gen.py
	}`

The command
	`proto`
then prompts for a filename, creates a directory of this name, and places all appropriately-renamed
files and subfolders within it. A minified copy of jquery is included for off-line development. 

The app is invoked from the command line with
	`python start.py`
from inside the app's folder. 

This starts a localhost server on port 8000 (if not already running) and opens the html page. 

The 'path' on line 21 of `proto_gen.py` will need to be modified to the directory in which the `proto`
folder is placed. 