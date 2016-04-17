`proto` is a web app prototype generator for creating a basic html/css/javascript/jquery/python
framework for web apps, packaged with a python server set to run on localhost. 

The program can be invoked from any directory by using a bash script
such as `proto(){python file-path-to-proto-folder/proto_gen.py}`. 

The command to run the `proto` program is then simply `proto`. 

The script `proto_gen.py` requests a new file name and copies the contents of the proto folder
into a newly created folder that has this new name; all files in the new folder are renamed 
according to the user-specified name. 