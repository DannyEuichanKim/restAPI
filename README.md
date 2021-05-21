# restAPI
This is done using Python and the package Flask. 
This is still a work in continuation, but the current code should work. Future optimization will be made soon
For example, the requirements.txt will be added soon, and the code will be improved

The server location for this is http://127.0.0.1:5000/
After running app.py, open another terminal and type:
curl http://127.0.0.1:5000/"location of json file"
The program takes in the json file location, writes the json file in reverse, and then puts the json string. 
The code system exits with an error if the json body is not a string, but writes and puts reversed string otherwise. 
