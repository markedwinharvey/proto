<h4>proto</h4>
<h5>proto</h5>


Usage:

	$ python proto/start.py [optional-port-number]
	Initializing server
	Starting new python server on port [####]...


The default browser loads proto.html via http://localhost:####/proto in a new window

	
Navigating to the web console, you should see something like:
	
	Received the following data from proto.py:
	Object { project_name : "proto" } 


In that case, the frontend is communicating with python (proto.py) via jquery's $.ajax (in proto/static/proto.js)
	



Installation:
	
	$ python setup.py install