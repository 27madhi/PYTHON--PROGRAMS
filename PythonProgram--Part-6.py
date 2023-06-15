l1=[20,30,40,50,60]
l2=[30,40,50,60]
len1=len(l1)
len2=len(l2)
print(len1,len2)
if (len1>len2):
    for i in range(1,len1-len2+1):

        l2.append(0)
    print(l2)
else:
    for i in range(1,len2-len1+1):
        l1.append(0)
print(l1)
print(l2)
l4=[]
if(len1>len2):
    for i in range(0,len1):
        l4.append(l1[i]+l2[i])
        print(l1[i]+l2[i])
else:
    for i in range(0,len2):
        l4.append(l1[i]+l2[i])
print(l4)

def addr(*mad):
  return addr


print(addr(madhi='ch',Kam='thu'))

def name(**wrd):
   Sum=''
   for i ,k in wrd.items:

      print(i,k)


name(n='madhi',l='vino',d='sugan')

'''fibonaacii series '''
n= int(input("enter a number:"))
F1= 0
F2=1
for i in range(1,n+1):
   F3=F1+F2
   print (F3)
   F1=F2
   F2=F3
   F3=F2

'''without recursion '''
def fib(n):
  if n<=1:
    return 1

  return (fib(n-1)+fib(n-2))
n= int(input ("enter"))
for i in range(n):
  print (fib(i))





A= [20,30,40,50,60]
S=iter(A)
S.__next__()
while (S):
   try:
      print(next(S))
   except StopIteration :
      print ("end")
      break

def Mygen(n):
   for i in n:
      print(i)
      print (":")

      yield i**2
n=[2,3,4,5,6]
for j in Mygen(n):
    n=j
    j+=0


    print (n,j )

def fac(n):
   for i in range(1, n+1):
      i+=1*i
      yield i
n=30


for j in fac(n):
   print(j)

import math

def primeCheck(x):
sta = 1
for i in range(2,int(math.sqrt(x))+1): # range[2,sqrt(num)]
 if(x%i==0):
  sta=0
  print("Not Prime")
  break
 else:
  continue
 if(sta==1):
  print("Prime")
  return sta

num = int(input("Enter the number: "))
ret = primeCheck(num)

def fac(n):
   for i in range(1, n+1):
      i+=1*i
      yield i


for j in fac(10):
   print(j)

def prm():
   H=2,3,5,7,11
   print(type(H))
   n=list(H)
   return(n)
prm()

def prm(n):
  for i in range (1,n+1):
    if n % i== 0:
       print("it's not a prime number")
    else:
       print ("number is prime number")
       l.append(i)


       return l

n=
l=[]
print(prm(n))

i = 1
x = int(input("Enter the number:"))
for k in range(1, x+1):
    c = 0
    for j in range(1, i+1):
        a = i % j
        if a == 0:
            c = c + 1

    if c == 2:
        print(i)
    else:
        k = k - 1

    i = i + 1

n= int(input( "enter a number"))
  for n in range(1,Num):
    for i in range(2,n):
      if n%i ==0:
        break
   else:
     print (n)

for i in range(2,4):
  flag=0
  print ("i=",i)
  for j in range(2,i):
    print("j=",j)
    i%j==0
    flag=0

lst1=[ "Levis","HM","Allen Solly"]
lst2=["tshirt","jacket","blazers"]
for m in lst1:
  for n in lst2:
    print (m,n)

for i in range (2,):
  print (i)





for i in range(1,6):
   for j in range (1,3):
      print(j, end='')
   print ()

n=6
for i in range(1,n+1):
  for j in range(1,n+1-i):
    print(" ",end="")
  for k in range(1,i+1):
    print("*",end=' ')
  print()





for i in range(5,0,-1):
  for j in range(i,):
    print (i, end='')
  print()

num=5
Min=5
for i in range(1,6):
  Min=5
  for j in range(i):


    print(Min,end='')
    Min-=1

  print( )
print('completed the pattern')

n=1

while True:
  if n<=10:
    print("belive in yourself")
    n+=1

N= int(input ("enter the number:"))
while True:
  if N % 20==0

for i in range (2,4):
  print("i=",i)
  for j in range (2,i):
    print ("j=",j)

'''write a function to list a
 first N prime number '''
def prm(n,lst):
  for i in range(2,n+1):
    count=0
    for j in range (2,i):
      if i%j==0:
        count+= 1
        print(i,"nt prime number")
        break
    if count==0:

      return(


n= 10
lst=[  ]

print(prm(n,lst,))

