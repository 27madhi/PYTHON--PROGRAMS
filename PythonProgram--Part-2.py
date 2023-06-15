'''fibonaccii series'''
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci (n-2)

for i in range (1,7+1):



    print (fibonacci(i))

'''nested function '''
def first(n):
    if n==20:
        print ("equal 20")

    def second(n):

        n=n*n
        print (n)
        def third(n):
            n=n+n
            print (n,"hello")
            def fourth(n):
                print (n+200)

            fourth(n)

        third (n)
    second (n)




#Number=first(20)
#print(Number)
first(20)

a= [11,14,21,56,78,45,29,28]
x = lambda a: a%2 == 0
y = lambda a: a%2 != 0
z = lambda a: a%3 == 0
print (x)

def mainfunc(func):
    def innermain(a):
        print ("executing")
        func()

        print ("executed")
        return "hello"

    return innermain

def madhi():
    print ("hello my dear family 💐🤗 ")
family= mainfunc(madhi)

family



def div_receiver(fun):
    def div_mainfunc(x,y):
        if y==0:
            return "you can't divide by zer0"
        return fun(x,y)
    return div_mainfunc

@div_receiver
def div(a,b):

    return a/b

print (div(4,0))

def divhas_arg(func):
    def innerdiv(x,y):
        if y==0:
            print (" youcan't multiple by zer0")
            return "you can't "
        else:
            return func(x,y)
    return innerdiv


@divhas_arg
def div(no1,no2):
    return no1*no2
print(div(10,5))

for i in range (3):
   print (i)



def h(gh):
   print("hello")
   gh()
   return

def m():
   print ("guys")
g=h(m)

import odd

def isodd(n):
    if n%2!=0:
        return n




def my_func(fun,lst):
    res=[]
    for i in lst:
        Val=fun(i)
        if Val!=None:
            res.append(Val)
    return res

L=[1,2,3,4,5,6]
Od=my_func(odd.isodd,L)
print (Od)

'''Generator'''


def FirstNnumber(n):
    N=1
    while N<=n:
        yield N
        N=N+1
sequence=FirstNnumber(10)
print (next(sequence))
print (next(sequence))
for j in sequence:
    print (j)

'''generator data processing time
taken
'''
import random
import time


names=['madhi','kamal','sundar','nadella']
colors=['red','yellow','blue','green']



def students_l(numof_people):
    result=[]
    for i in range(numof_people):
        stu={ 'id':i, 'name':random.choice(names),'color':random.choice(colors)
             }
        result.append(stu)
    return result


def students_gen(numof_people):
      result=[]
      for i in range(numof_people):
          stu={'id':i,'name':random.choice(names),  'color': random.choice(colors)
              }
          result.append(stu)
      yield result
time1=time.process_time()
students= students_gen(10)
time2=time.process_time()
print (next(students))


for i in students:

    print (i)

print ('time taken :',time2-time1)

import math

Num=int(input ('enter a number:'))
fac=math.factorial(Num)
print (fac)

try:

    print (fac)
except ValueError:
    print ('cant validate character ')
finally:
    print ('complete kudos')
try:
    n

    print (fact)
except Exception as e:
    print (e)
finally:
    print ('complete kudos')

try:


    print (fact)
except Exception as e:
    print (e)
else:
    print ("work done")

finally:
    print ('complete kudos')

'''Exception Handling '''
import math

Num=int(input ('enter no:'))

try:
    fac=math.factorial(Num)
    print (fac)


except ValueError:
    print ('cant validate negative Number')
else:
    print ('work done')
finally:
    print ('complete kudos')
try:
    n
    fac=math.factorial(Num)
    print (fac)

except Exception as e:
    print (e)
finally:
    print ('complete kudos')

try:
    fac=math.factorial(Num)
    print (fac)

except Exception as e:
    print (e)
else:
    print ("work done")

finally:
    print ('complete kudos')

import os
dir(os)

os.getcwd()

import random
l=len(dir(random))
print (l)
rand=[]
for i in range (l):

    if i <=l:

        rand.append(dir(random))

print (rand)

"""MODULES
  1. RANDOM MODULES:
    1. dir(random) shows methods in random
    2. random.random() gives float
       value 0.0 to 1.0.
    3. random.uniform( 10,20)
       gives float valve for give num.
    4. random.randint(1,10)
       gives value for given range.
    5. random.randrange(1,10,2)
        here we can give step value
    6. random.choice() it's can't give a value morethan one.
    7. random.choices(listname, weights=[ 1,3,4],k=5)
    8. random.getrandbit(4)
        min=0000,max=1111=15
        it's can give value based bits.
    9.random.shuffle()
    10.random.sample(varname,k=10)
        get specific values
"""

'''RANDOM MODULES '''
#choices()


import random
label=["green","red","blue","black"]
#here I used choices() method

Choices=random.choices(label,weights
=[ 3,1,2,4] , k=10)

print (Choices)



from datetime import*

Datetime= [dir(datetime)]

for i in Datetime:
    print (i)
print (datetime.today())

from datetime import *
td= datetime.now()
print (td)
mytime= td.strftime("%d/%B/%y")
print (mytime)
time= datetime.strptime(mytime,"%d/%B/%y")
print (time)





n= int(input ("enter the prime number"))
h=[]

def list():

  for i in range (1,n):



    for j in range (2,i):
      if i%j==0:
        break

    else:
      print([i ,end=',')







print(list())

n= int (input ("enter a number"))
for i in range (1,6):
  i*20>=n
print ()

G=int(input("enter a number to check fib num or not"))
N=10
a=-1
b=1

for i in range (1,N+1):

   print (a+b,"is Fibonacci series")
   b=a+b
   a= b-a

if a+b==G:
   print ("it's fib series number,hurray great work ")
else :
   print("it's not fib series number,try it again ")

for j in range (3):
  print(j)

def list():
 n= int(input("enter a prime number"))
 l=[]
 for i in n :
  n=int(input ("enter a number "))
  l.

n = int(input("enter a number"))

l=[]

for i in range (n):



  l.append(i)

  print (l)

import time
import datetime
print("Current date and time: " , datetime.datetime.now())
print("Current year: ", datetime.date.today().strftime("%Y"))
print("Month of year: ", datetime.date.today().strftime("%B"))
print("Week number of the year: ", datetime.date.today().strftime("%W"))
print("Weekday of the week: ", datetime.date.today().strftime("%w"))
print("Day of year: ", datetime.date.today().strftime("%j"))
print("Day of the month : ", datetime.date.today().strftime("%d"))
print("Day of week: ", datetime.date.today().strftime("%A"))

n= 30
while n>=20:
  if n % 20 ==0:
    print (n)
    n+=1

'find multiple of 20 using break'''

n=20
l= []
while n >= 20:
   if n % 20==0:
      l.append(n)

      if n>100:
         break
   else :
       print (" number is not multiple of 20")


print(l)
print ("successfully completed" )

row=5
while row>=1:
    col=5

    while col>=row:
        print (row,end='')
        col-=1
    print ()
    row-=1

row=5
value=1
while row>=1:
    col=1

    while col<=row:
        print ('-',end='')

        col+=1
    print (value,end='')
    value+=1
    print ()
    row-=1

row=5

while row>=1:
    col=1


    while col<=row:
        print ('-',end='')
        col+=1
    value =5
    while value>=row:
        print (row,end='')
        value-=1
    print ()

    row-=1