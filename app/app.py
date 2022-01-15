import flask

import userAPI, chatAPI
import filemanager as fs
import hashlib

app = flask.Flask(__name__)


@app.route('/login')
def login():
  username = flask.request.args.get('username', 0, type=str)
  password = flask.request.args.get('password', 0, type=str)
  output = userAPI.login(username, password)

  tok = -1

  if output[0] == True:
    tok = hashlib.sha3_512(fs.get("userdata.txt", username).encode()).hexdigest()

  return flask.jsonify(status=output[0], message=output[1], token=tok)


@app.route('/')
def index():
  return flask.render_template('index.html')

@app.route('/signuphtml')
def signuphtml():
  return flask.render_template('signup.html')

@app.route('/signup')
def signup():
  username = flask.request.args.get('username', 0, type=str)
  password = flask.request.args.get('password', 0, type=str)
  output = userAPI.signup(username, password)
  return flask.jsonify(status=output[0], message=output[1])

@app.route('/chathtml')
def chathtml():
  return flask.render_template('chatroom.html')

@app.route('/postmessage')
def postmessage():
  username = flask.request.args.get('username', 0, type=str)
  token = flask.request.args.get('token', 0, type=str)
  message = flask.request.args.get("message", 0, type=str)

  opStatus = False
  opMsg = "Unknown"

  if token == hashlib.sha3_512(fs.get("userdata.txt", username).encode()).hexdigest():
    opStatus = True
    opMsg = ""
    message.replace("\n", "")
    if message != "":
      chatAPI.sendMessage(username, message)
  else:
    opMsg = "Invalid Token"
  return flask.jsonify(status=opStatus, message=opMsg)

@app.route('/getmessages')
def getmessages():
  messgs = chatAPI.getMessages()
  return flask.jsonify(messages=messgs)