import filemanager as fs

def getMessages():
  filename = "messages.txt"
  messageList = fs.mass_get(filename)
  messageString = ""
  for message in messageList:
      messageString += message[0] + ": "+message[1]
  return messageString

def sendMessage(username, message):
  filename = "messages.txt"
  fs.append(filename, username, message + "\n")

def messageSendFunction(username):
  while True:
    message = input()
    message.replace(': ', " ")
    sendMessage(username, message)