import filemanager as fs
import threading
import util
import time

def getMessages(auth):
  filename = "messages.txt"
  messageList = fs.mass_get(filename)
  messageString = ""
  for message in messageList:
    if message[0] == auth.lower():
      messageString += "\u001b[96m" + message[0] + "\u001b[00m: " + message[1]
    else:
      messageString += "\u001b[92m" + message[0] + "\u001b[00m: " + message[1]
  return messageString

def sendMessage(username, message):
  filename = "messages.txt"
  fs.append(filename, username, message + "\n")

def messageEventFunction(username):
  file = "messages.txt"
  lastmsg = fs.last_entry(file)
  while True:
    time.sleep(0.1)
    if lastmsg != fs.last_entry(file):
      lastmsg = fs.last_entry(file)
      util.clear()
      print(getMessages(username))

def messageSendFunction(username):
  while True:
    message = input()
    message.replace(': ', " ")
    sendMessage(username, message)

def chatService(username):
  util.clear()
  print(getMessages(username))
  recieve = threading.Thread(target=messageEventFunction, args=(username,))
  send = threading.Thread(target=messageSendFunction, args=(username,))
  recieve.start()
  send.start()
  time.sleep(99999)