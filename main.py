import subprocess
with open("run.sh", "rb") as file:
  script = file.read()
rc = subprocess.call(script, shell=True)

#the only purpose of this file is to run the flask app via the replit shell

#the acutal code of this project is stored in the following files
"""
Python:
  -/app/app.py (All of the flask programming, including all app routes)
  -/app/filemanager.py (Simple toolkit i made for interfacing with text files like a database)
  -/app/userAPI.py (Toolkit i made for managing user login/signup attempts)
  -/app/chatAPI.py (another toolkit i made for easy management of messages)

HTML/JS:
  -/app/templates/index.html (Homepage/Login page)
  -/app/templates/signup.html
  -/app/templates/chatroom.html
  -/app/static/jquery.js (Not my library, this is a common JS library i use in the project)

CSS:
  -/app/static/chat.css (chatroom stylesheet)
  -/app/static/default.css (login and signup stylesheet)

Other:
  -/app/favicon.ico
  -/app/userdata.txt (File where usernames and passwords are stored)
  -run.sh (file containing the script to run in order to run the flask app)

"""