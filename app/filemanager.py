#This is my homemade file function kit
#It contains a bunch of functions i can use to store data for this project

def findkey(key, data):
  #takes a key and array of datalines
  #returns the dataline that the key corresponds to
  output = ""
  for line in data:
    line = line[0:len(line)-1]
    dat = line.split(": ")
    if dat[0] == key:
      output = dat[0] + ": " + dat[1]
  if output == "":
    output = -1
  return output

def locatekey(key, data):
  #takes a key and array of datalines
  #returns the position of the dataline the key corresponds to in the array
  output = -1
  i = 0
  for line in data:
    line = line[0:len(line)-1]
    dat = line.split(": ")
    if dat[0] == key:
      output = i
    i += 1
  return output

def readFile(filename):
  file = open(filename, "r+")
  data = file.readlines()
  file.close()
  return data
  






def write(filename, key, value):
  #takes a key and a value
  #assigns the value to that key
  value = str(value)
  if " " in key: return False
  else:
    file = open(filename, "r+")
    data = file.readlines()
    file.close()
    file = open(filename, "w")
    lineid = locatekey(key, data)
    output = True
    if lineid == -1:
      data.append(key + ": " + value + "\n")
      towrite = ""
      for line in data:
        towrite += line
      file.write(towrite)
      file.close()
    else:
      data[lineid] = key + ": " + value +"\n"
      towrite = ""
      for line in data:
        towrite += line
      file.write(towrite)
      file.close()
    return output

def append(filename, key, value):
  #same as write, but allows for mutliple keys to be the same
  #appends the value and key to the file
  value = str(value)
  if " " in key: return False
  else:
    file = open(filename, "a")
    output = True
    towrite = key + ": " + value + "\n"
    file.write(towrite)
    file.close()
    return output


def get(filename, key):
  #takes a key
  #returns the value of that key
  file = open(filename, "r+")
  data = file.readlines()
  file.close()
  line = findkey(key, data)
  output = []
  if line == -1: output = "□"
  else:
    dat = line.split(": ")
    output = dat[1]
  return output

def mass_get(filename):
  #takes only a filename
  #returns a list of lists of keys and values
  file = open(filename, "r+")
  data = file.readlines()
  file.close()
  output = []
  for line in data:
    if ": " in line:
      dat = line.split(": ")
      output.append([dat[0], dat[1]])
  return output

def last_entry(filename):
  #takes only a filename
  #returns the value of the last entry in that file
  file = open(filename, "r+")
  data = file.readlines()
  file.close()
  finder = True
  i = 0
  v = ""
  while finder:
    if ": " in data[len(data)-i-1]:
      v = data[len(data)-i-1].split(": ")[1]
      finder = False
    i+=1
    if len(data)-i-1 < 0:
      finder = False
  if v == "": v = -1
  return v



