# Chatroom App
### Python Final Project

This is a project made using four languages, Python, Javascript, HTML, and CSS.
I use Python library flask to host the server and handle HTTP requests. Python is used to read and compare data as well as store data, and also to proccess http requests. Javascript it used to interface between Python and HTML. HTML is used for making the website, and CSS to make it look how it does.

The end result is a chatroom with fully functional and semi-secure logins and message data.t

The only file that is not my own code is /app/static/jquery.js, it is a common and open-source Javascript library i downloaded for use in this project.



-------------------------------------
# File Breakdown

### Python
- main.py, used to start the flask app when run on replit
- /app/app.py, the actual host of the flask app and the central program in all of this, controlling HTTP requests and communications between the webpage (Javascript) and python
- /app/filemanager.py, the toolkit I made for easily interfacing with text files like a database
- /app/userAPI.py, the toolkit I made for simplifying the management of user/login related actions
- /app/chatAPI.py, the toolkit I made for managing chat/message related actions

### HTML/CSS
- /app/templates/index.html, The default/login page
- /app/templates/signup.html, The sign up page
- /app/templates/chatroom.html, The actual chatroom page
- /app/static/chat.css, The stylesheet used by chatroom.html
- /app/static/default.css, The stylesheet used by index.html and signup.html

### TXT
- /app/userdata.txt, Where all the usernames and encrypted passwords are stored
- /app/messages.txt, Where all the messages are stored

### Other
- /app/favicon.ico, An image used in the webpages
- run.sh, the file containing the script used by main.py to run the app

Note: all the files in the v1 folder are meant for the old version of this project which would run in the python console, and should be ignored.