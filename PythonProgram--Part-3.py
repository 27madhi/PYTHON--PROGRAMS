'''regular Expression '''

from re import*
num="hello my 08825759352"

mobnum_pattern=compile("(0|91)?[6-9][0-9]{09}")
print (mobnum_pattern)
num_present= mobnum_pattern.search(num)

print (num_present)

from re import *




landline_num= compile(r'((91)((\d){3,5}))-([1-9][0-9]{4,7})')
numsearch=landline_num.search("9123678-27876")
print(numsearch.groups())

import re
landLinePattern= re.compile(r'((91)((\d){2,4}))-([1-9][0-9]{5,8})')
present = landLinePattern.search ( '914462-521121')
print (present.groups())
print (present.group(5))

import re

def isMobileNumber(sentence):
   mobileNumberPattern =re.compile("(91[6-9][0-9]{9})")
   number = mobileNumberPattern.findall(sentence)
   return number
sentence = "My mobile no is 918344777333 and 918883775533, 91234567890"
mobileNumber_present = isMobileNumber(sentence)
print (type (mobileNumber_present) )

for eachnumber in mobileNumber_present:
   print (eachnumber)

import re
datePattern = re.compile(r'([0-3][0-9])/([0-1][0-2])/((\d){4})')
dateFound = datePattern.search('My birthdate is 28/10/2022')
if not dateFound is None:
    print(dateFound.groups())
    day = dateFound.group(1)
    month = dateFound.group(2).lstrip("0") # strip என்ன செய்யும் என்று கொஞ்சம் சிந்தியுங்களேன்.
    print (month)
    year = dateFound.group(3)
    print(day, month, year)
    if int(month) in [1,3,5,7,8,10,12]:
        if int(day)>31:
            print("Invalid Date, Date can't be greater than 31")
    elif int(month) in [4,6,9,11]:
        if int(day)>30:
            print("Invalid Date, Date can't be greater than 30")
    else:
        if int(day)>29:
            print("Invalid Date, Date can't be greater than 29")
        elif int(day)==29:
            y = int(year)
            if not (y%4) ==0:
                print("invalid date")

else:
    print("Invalid Date")
print ("right!")

from re import *

def passwordchecker(password):
    if len(password)<8:
        print("password must contains 8 or more characters")
    else:
        if search("[a-z]", password) and search ("[A-Z]", password) and search( "[0-9]", password):
            print ("strong password")

        else:
            print("character should be in both upper and lower character and atleast one character")





password= "Madhiyazhagan123"

passwordchecker(password)

"""
\s=space
\.= sentence"""



import re
def wordCount(sentence):
    pattern = re.compile(r'\s')
    space = pattern.findall(sentence)
    print (space,len(space))
    return len(space)
sentence =input()
count = wordCount(sentence)
print (sentence, " contains ", count, "Words")



"""
\s=space
\.= sentence
\S= nospace

"""



import re
def wordCount(sentence):
    pattern = re.compile(r'\s')
    space = pattern.findall(sentence)
    print (space,len(space))
    return len(space)+1
sentence = "python is easy"
count = wordCount(sentence)
print (sentence, " contains ", count, "Words")

import re

def sentenceCount(sentenc): #3
  pattern = re.compile(r'\.') #4
  space = pattern.findall(sentenc)
  print(space)#5 முற்றுப்புள்ளியைத் தேடும்
  return len(space) #6 ஏன் len பார்க்கிறோம்? space str வகை அல்லவா!

sentence = "hello mam.whatsup a day."#input("Enter your sentence: ") #1
count = sentenceCount(sentence) #2
print(sentence, " contains ", count , " sentence(s)")

from re import *


def findmail(mailid):
    for i in mailid:
        pattern=findall("[0-9]\S+@\S+",mailid)
    return pattern

mailid="mailidOnline Python compiler (interpreter) to run Python online. 27madhi27madhi@gmail.com . Write Python 3 code in this online editor and run it."
gotmailid=findmail(mailid)
print(type(gotmailid))
print(gotmailid)
for i in gotmailid:
    print (i)

import re, urllib
import urllib. request
webpage = urllib.request.urlopen("https://www.redbus.in/info/contactus")
data = webpage.read ()
phoneNumbers = re.findall("[0-9-1{7}[0-9-]+",str(data),re.I)
print(phoneNumbers)

'''iterator mainly used for memory spaces'''
it=[120000,110000,130000]
h=it.__iter__()
#for i in it:
   #print (i)
while(h):
   try:
      print(next(h))
   except StopIteration:
      print ("iteration stopped")
      break

"iterator object creation"
class top20values:
    def __init__(self):
        self.num=1
        self.num1=1
        self.num2=self.num+self.num1

    def __iter__(self):
        return self
    def __next__(self):
        if self.num2<=20:
            Val= self.num2
            self.num2+=1
            return Val
        else:
            raise StopIteration
Values=top20values()
for i in Values:
    print (i)

'''map function
   format map(funcname,list) it's
most used for  giving  vary argument
Value to the function.'''
def myfun(n):
   return n+n
H = list(map(myfun, [1,2,3]))
print (H)
for i in H: and
   print (i)

'''filter function mainly used for
the function argument is the true
then return value or otherwise
 false return
format: filter(func name,list)'''
def myftf(n):
   if n%2!=0:
      print (n)
F=filter(myftf,[1,3,4,5,6,7])

print(F)

from time import*
from threading import*

class welcome(Thread):
   def run(self):
      for i in range(5):
         print ( "welcome")
         sleep(0.2)

class bye(Thread):
   def run(self):
      for i in range(5):
         print ("bye")
         sleep (0.2)
t1=welcome()
t2=bye()




t1.start()
sleep(0.2)
t2.start()

#print(current_thread().getname(t1))



'''reduce function'''
from functools import*
def my_add(a, b):
   result = a + b
   print(f"{a} + {b}= {result}")
   return result

lis =
H = reduce(my_add,lis)
print (H)

'''multithreading'''
from threading import *
from time import *




def trasig_red():
   print("show stop")

   print("stop all the vehicle")



def trasig_green():
   print("show green")

   print("allow all vehicle to go ahead")
T1= Thread(target=trasig_red)
T2=Thread(target=trasig_red)
T1.start()

T2.start()

T1.join()
T2.join()

"""from cryptography.fernet import Fernet
key = Fernet.generate_key()
f = Fernet(key)
token = f.encrypt(b"my deep dark secret")
print (token)
Decry=f.decrypt(token)
print (Decry)"""

"""Password manager"""
from cryptography.fernet import Fernet

key = Fernet.generate_key()
with open("key.key", "wb") as key_file:
    key_file.write(key)


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:",
                  fer.decrypt(passw.encode()).decode())


def add():
    name = input('Account Name: ')
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input(
        "Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue

"""import sys
from pytube import YouTube"""

"""random password generator"""
import string
import random
character=list(string.ascii_letters + string.digits + "$&@#£€¥")
print(character)


def generate_password():
    passw_len=int(input("how long would you like your password to be: "))


    password=[]

    for i in range(passw_len):
        password.append(random.choice(character))


    random.shuffle(password)

    passw= "".join(password)
    print (passw)



user=input("do you want to generate password,then enter yes/no: ").lower()
print (user)
if user == 'yes':
    generate_password()
elif user== 'no':
    print( "Not generate the password")
    quit()
else:
    print("please enter yes/no")
    quit()