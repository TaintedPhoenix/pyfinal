#This is kit of functions for dealing with user data & logins/signups

import filemanager as fs
#see filemanager.py
import hashlib
#used for making sure passwords cannot just be read from a file, hashes text
import time

def login(username, password):
  #takes a username and password
  #determines if the person owns the account
  output = [False, "Unknown Error"]
  data = fs.readFile("userdata.txt")
  if fs.findkey(username, data) == -1:
    output = [False, "Invalid Username"]
  else:
    hashpass = fs.get("userdata.txt", username)
    if hashlib.md5(password.encode()).hexdigest() == hashpass:
      output = [True, ""]
    else:
      output = [False, "Invalid Password"]
  return output

def signup(username, password):
  #takes a username and password
  #makes a new account
  output = [False, "Unknown Error"]
  data = fs.readFile("userdata.txt")
  if fs.findkey(username, data) != -1:
    output = [False, "Username is taken"]
  else:
    hashpass = hashlib.md5(password.encode()).hexdigest()
    fs.write("userdata.txt", username, hashpass)
    output = [True, ""]
  return output

def isUser(username):
  #takes a username
  #determines if an account with that username exists
  output = True
  data = fs.readFile("userdata.txt")
  if fs.findkey(username, data) == -1:
    output = False
  return output

def loginSequence():
  #Triggers a login sequence, returns the username of the account upon successful login
  print("Welcome to the chatroom!\n")
  logina = True
  while logina:
    print("\nPlease log in: \n")
    username = input("Username: ")
    if " " in username:
      print("\n\u001b[31mUsername cannot contain spaces.\u001b[00m")
    elif isUser(username) == False:
      choice = input("\nInvalid Username. Would you like to sign up? (Y/N): ")
      if choice.lower() == "y":
        passwordselection = True
        while passwordselection:
          password1 = input("\nEnter a password: ")
          password2 = input("Confirm password: ")
          if password1 != password2:
            print("\nPasswords do not match. Please try again.")
          else:
            signupg = signup(username, password1)
            if signupg[0] == False:
              print(f"\u001b[31merror: {signupg[1]}\u001b[00m")
            passwordselection = False
            print("\nThank you for signing up!")
    else:
      password = input("Enter password: ")
      loginb = login(username, password)
      if loginb[0] == False:
        print(f"\u001b[31merror: {loginb[1]}\u001b[00m")
      else:
        print("\n\u001b[92mLogin Successful.\u001b[00m")
        print(f"Welcome {username}!")
        logina = False
        time.sleep(2)
        return username
