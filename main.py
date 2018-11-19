#########################################################################
#To Do:
# -Add modifier based on position within string
# -Make better randomized charcter positions (based on total length?)
# -Add more randomized characters
#########################################################################

import random
count = 0

def Encrypt():
  password = input("Password:")
  maxCount = int(input("Number of encryptions (<994)"))
  passnum = 1
  for i in range(len(password)):
    if i == len(password)-1:
      passnum *= ord(password[i])*((i+1)**2)*(ord(password[0]))
    else:
      passnum *= ord(password[i])*((i+1)**2)*(ord(password[i+1]))
  passnum = int(passnum / 100000000000)
  messageOut = chr(random.randrange(32,126))
  file = open("Normal.txt", "r")
  messageIn = file.read()
  file.close()
  for i in range(len(messageIn)):
    currLetter = ord(messageIn[i])*passnum
    currLetter = (currLetter%95)+32
    messageOut += chr(currLetter)
  messageOut += chr(random.randrange(32,126))
  global count
  count += 1
  encrypt(messageOut,passnum,maxCount)
################################################################
def encrypt(messageIn,passnum,maxCount):
  messageOut = chr(random.randrange(32,126))
  for i in range(len(messageIn)):
    currLetter = ord(messageIn[i])*passnum
    currLetter = (currLetter%95)+32
    messageOut += chr(currLetter)
  messageOut += chr(random.randrange(32,126))
  global count
  count += 1
  if count == maxCount:
    file = open("Encrypted.txt", "w")
    file.write(messageOut)
    file.close()
  else:
    encrypt(messageOut,passnum,maxCount)

#################################################################

def Decrypt():
  password = input("Password:")
  maxCount = int(input("Number of encryptions"))
  passnum = 1
  for i in range(len(password)):
    if i == len(password)-1:
      passnum *= ord(password[i])*((i+1)**2)*(ord(password[0]))
    else:
      passnum *= ord(password[i])*((i+1)**2)*(ord(password[i+1]))
  passnum = int(passnum / 100000000000)
  file = open("Encrypted.txt", "r")
  messageIn = file.read()
  file.close()
  messageIn = messageIn[1:-1]
  messageOut = ""
  
  for i in range(len(messageIn)):
    messageOut += chr((((ord(messageIn[i])-32) * (egcd(passnum,95)[1] % 95)) % 95) +32)
    
  global count
  count += 1
  decrypt(messageOut,passnum,maxCount)

######################################################

def decrypt(messageIn, passnum,maxCount):
  messageIn = messageIn[1:-1]
  messageOut = ""
  
  for i in range(len(messageIn)):
    messageOut += chr((((ord(messageIn[i])-32) * (egcd(passnum,95)[1] % 95)) % 95) +32)
    
  global count
  count += 1
  if count == maxCount:
    file = open("Normal.txt", "w")
    file.write(messageOut)
    file.close()
  else:
    decrypt(messageOut,passnum,maxCount)
  

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)
  
def Start():
  run = input("Would you like to Encrypt or Decrypt?")
  if (run == "Encrypt") or (run == "encrypt") or (run == "e") or (run == "E"):
    print("Encrypting")
    Encrypt()
  else:
    print("Decrypting")
    Decrypt()
