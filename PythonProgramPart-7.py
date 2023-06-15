from collections import namedtuple as nm
a=nm('courses',['name','technologyfield'])
d=('artificial intelligence','python')
print (d)

'''find a maximum of two number '''

n1= -5
n2= -10
if n1>n2:
  print (n1,"=n1 is great than n2")
else:
  print (n2,"= n2 is great than n1")

'''factorial series'''
N= 105
fact= 1
Ls=[]
for i in range (1,N+1):
  fact=fact*i
  Ls.append(fact)
print(Ls)





def Fibonacci(n):
    if n<= 0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

# Driver Program

print(Fibonacci(10))

# This code is contributed by Saket

N=10
a=-1
b=1

for i in range (1,N+1):

   print (a+b,"is Fibonacci series")
   b=a+b
   a= b-a
G=


if a and b == G:
   print ("it's fib series number,hurray great work ")
else :
   print("it's not fib series number,try it again ")



'''Fibonaccii series'''

Num=7
F=0
S=1

if Num==F:
     print ("enter a positive        number to generate ")
for i in range(1,Num+1):

     print (F)
     T=F+S
     F=S
     S=T

'''fibonaccii series'''
a,b=-1,1
count=int(input ("enter a number"))
while count>0:
    t=a+b
    print (t)


    a=b
    b=t
    count-=1

'''fibonaccii series'''
a,b=-1,1
count=int(input ("enter a number"))
while count>0:
    t=a+b
    print (t)
    if t==count:
        break

    a=b
    b=t

a= -1
b= 1
count= int(input("enter a number "))
for i in range ( count):
    print (a+b)
    b=a+b
    a=b-a
'''fibonaccii series without thirsd variable'''

while row>=1:
    col=0
    while col<row:
        print (row+col,end=' ')
        col+=1
    print ( )
    row-=1

''' decimal to binary number '''




no= int(input ("enter a number"))
while no>0:
   rem=no%2
   print (rem)
   no=no//2

def condi(C):
   if C>=5:
      print ("c")

      return (C**2)
M=list(filter(condi,[4,3]))
print(M)

def cube(N):
    return (N**3)

for i in map(cube,[1,2,3,4,5]):
    print(i)

n=10
for i in range (1,n):
  for j in range (2,n):
    if i%j==0:
      break
  else:
    print (n)

'''list comprehension'''
'''Lst= [i for i in range (1,11) if i%2==0]
print (Lst)'''

LF=[  for i in range (1,11) lam

A= lambda a:a**2
for i in range(1,11):

Sum=[1,2,3,4,5]
G=[0]
for i in range (1,6):

Add=[1,2,3,4,5]
Sum=[]
for i in Add :
  print (i)
  Sum=sum(i)

Arr=[1,2,3,4,5]
Ar= sum(Arr)
print (Ar)

Arr=[]
A=int(input ("enter a number:"))
for i in range (1,A+1):
  l= int(input ("enter:"))
  Arr.append(l)

print (Arr)

try:
  f= open("Device storage//documents//sample.docx","r")
  print( f.read())
  print (f.closed)
except Exception:
  print ("syntax error ")
finally:
  print("hello")

Name="Kamal"
I=0
while I<len(Name):
   print (Name[I],end='-')
   I=I+1

a=1
while a<=10:
 print ("hello")
 a+=1

L=[[1,2,3],
   [4,5,6],
   [7,8,9]]
for i in range(3):
    for j in range(3):
        print (L[i][j])

l=[1,2,3,4,5]

R=len(l)-1

while R>=0:
    print(l[R])
    R-=1

'''lcm'''
no1=int(input ("enter a number "))
no2=int(input ("enter a number "))
big=no1 if no1>no2 else no2
while True:
   if big%no1==0 and big % no2==0:
       print ("least multiple number",big)
       break
   big+=1

row=5

while row>=1:
    col=1


    while col<row:
        print ('',end=' ')
        col+=1
    value =5
    while value>=row:
        print ('*',end='')
        value-=1
    print ()

    row-=1

row=5

while row>=1:
    col=1


    while col<=row:
        print ('  ',end=' ')
        col+=1
    value =1
    while value<=row:
        print (value,'  ',end='  ')
        value-=1
    print ()

    row-=1

row=1

while row<=5:
    col=1

    while col<row:
        print ('-',end=' ')
        col+=1

    value =1
    while value<=row:
        print (value,end=' ')
        value+=1
    print ()
    row+=1

row=1

while row<=5:
    col=1


    while col=row:
        print ('',end=' ')
        col+=1
    value =1
    while value<=row:
        print (value,end=' ')
        value+=1
    print ()

    row+=1