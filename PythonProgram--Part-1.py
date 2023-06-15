Top left part of Diamond
"""

row=5
col2=1

while row>=1:
    col=1
    while col<=row:
        print (row,end=' ')
        col+=1
    print ()
    row-=1

"""Top right part of Diamond"""

row=0

while row>=1:


    col2=1
    while col2<=row:
        print (col2,end=' ')
        col2+=1
    print ()
    row+=1


"""Down left side of diamond"""

row=5
col2=1

while row>=1:
    col=1



    while col<=row:
        print (' ',end=' ')
        col+=1
    value =1

    while value<=col2:
        print (value,end=' ')
        value+=1

    print ()
    col2+=1



    row-=1

row=5
row2=5
while row>=1:
    col1=1
    while col1<=row:
        print ('-',end=' ')
        col1+=1
    col2=5
    while col2<=row2:
        print (col,end=' ')
        col2+=1
    print ( )
    row2+=1
    row-=1

"""Down right side of diamond"""

row=1
col3=5
while row<=5:
    col=1
    while col<=row:
        print ('-',end='')
        col+=1
    col2=1
    while col2<=col3:
        print (col3,end='')
        col2+=1
    print ()
    col3-=1
    print ()


    row+=1

"""         Whole    Diamond"""

'''WHOLE PART OF DIAMOND'''


row=5
col2=1

while row>=1:
    col=1



    while col<=row:
        print (' ',end=' ')
        col+=1
    value =1

    while value<=col2:
        print ('∆',' ',end=' ')
        value+=1

    print ()
    col2+=1
    print ()
    row-=1

row=1
col3=5
while row<=5:
    col=1
    while col<=row:
        print (' ',end=' ')
        col+=1
    col2=1
    while col2<=col3:
        print ('∆',' ',end=' ')
        col2+=1
    print ( )
    col3-=1
    print ( )

    row+=1

'''string function (find) programs'''

quote='piython is very easy'
length=len(quote)

while True:

  position=quote.find('y', position+1,length)
  print( position)
  if position==-1:
      break

  print  ('position of y at',position)

n= 10
count=0
for i in range (2,n):
    count=0

    for j in range (2,i):

        if i%j==0:
           count+=1
           break

    if count==0:
        print(i)
    else:
        print (i,'is not prime')
''' prime number '''

S='madhiyazhagan'

print (S.replace('yazh','l'))

S= 'madhiyazhagan1234'
L= len(S)
print (L)
i=0
while True:
    if L!=i:
        print( True  )
        break
    i+=1


if L==i :
    print(False)

S= 'madhiyazhagan123345'
l=len(S)
i=0
while i<l:
    if S[i]>='a' and S[i]<='z':
        print('correct'  )
        break
    i+=1
else:
    print('False'  )

'''
A= "Mad"
l= len(A)
c=0
while c<l:
    if not A[c]>='a'and A[c]<='z':
        if not A[c]>='A' and A[c]<='Z':
            print("incorrect alpha"   )
            c+=1
            print(c )
            break

else:
    print("correct alpha" )'''

'''this logical is used to check whether
given input value is alphabet or not,
if not alphabet then it will show message
Called incorrect alpha '''
A= '123madhi'#
l= len(A)
p=0
c=0
while c<l:
    if not A[c]>='A'and A[c]<='Z':
        if not A[c]>='a' and A[c]<='z':
            print("incorrect alpha")

            print(p)
            p+=1
            break

    else:
        print("correct alpha" )
        break

'''reurn special characters'''
U="Madhi123@gmail.com"
L=len(U)
I= 0
while I<L:
    if not (U[I] >= 'M'and U[I] <= 'Z'):
        if not (U[I] >= 'a'and U[I] <= 'z'):
            if not (U[I] >= '0' and U[I] <= '9'):
                print(U[I])
    I+=1

''' return number'''
A="Madhi133"
P=0
c=0
while c < len(A):

    if not (A[c]>='A' and A[c]<='Z'):
        if not (A[c]>='a' and A[c]<='z'):
            print (A[c])
    c+=1


            #print(p)

mailid =" madhi23@#$"
i =0

while i<len(mailid):
 if not (mailid[i]>='a' and mailid[i]<='z'):
  if not (mailid[i]>='0' and mailid[i]<='9'):
   print (mailid[i], end=' ')
 i+=1

'''special character '''

mailid= "Madhi123@#$"
C =0

for i in mailid :
  if not (i>='a' and i<='z'):
    if not( i>='0' and i<='9'):
      print (i, end=' ')
      print (C,end=' ')
  C+=1

'''capital letter'''
A= 'madhiyzhagan'
print (A.lower())

'''lower to upper case character
Function '''
def upM(n):

  ch = n
  #print (ch)

  chup = ord(ch)
  #print (chup)

  chup = chup- 32
  #print (chup)

  M = chr(chup)
  #print( M)

  print("\nIts Uppercase is: ", M)
  return M
upM('k')



'''Merging two string'''
v= "VENKATAMUNI"
m="MADHIYAZHAGAN"
comb=''
l=len(v)
for i in range(0,l):
    if i<=l:
        comb=comb+v[i]
        i+=1
    if i<=l:
        comb=comb+m[i]
        i+=1
print (comb)
comb= comb+m[i:]
print (comb)

''' split letter and num'''
input= "27madhi27madhi"
l= len(input)
j1=''
j2=''
for i in input :
    if i.isalpha():
        j1+=i
    if i.isdigit():
        j2+=i
join=j1+j2
print (join)
#return join

input= "A5B6C7"
l= len(input)
j1=''
j2=''
for i in input :
    if i.isalpha():
        j1+=i
    if i.isdigit():
        j2+=i
join=j1+j2
print (join)
return join



"matrix"
m=[[10,20,30],
[40,50,60],
[70,80,90]]
t=[]
print ("before ")
for i in range (len(m)):
    for j in range (len(m)):
        print (m[i][j],end=' ')
    print ()

print ("after transport")
for i in range (len(m)):
    for j in range (len(m)):
        print (m[j][i],end=' ')
    print ()

print ("diagonal")
for i in range (len(m)):
    for j in range (len(m)):
        print (m[i][i],end=' ')
        t.append(m[i][i])
    print ()
print (t)

"bubble sort
l=[10,5,8,3]
i=0
j=1
print ("before ",l)
le=len(l)-1
for j in range (0,le):
    for i in range(0,le):

        if l[i]>l[i+1]:
            l[i],l[i+1]=l[i+1] ,l[i]
            print(l[i+1], l[i])
        print ("after bubble",l)


print (l)

'''Binary Search'''
L=[]
for h in range (1,32):
    L.append(h)
l=L
key= int(input ("enter a key to search"))
min=0
max=len(l)-1
while min<=max:
    avg= (min+max)//2
    if key==l[avg]:
        print ("key is presented at :",avg)
        break
    elif key>l[avg]:
        min= avg+1
    elif key<l[avg]:
        max= avg-1
else:
    print ("key is not present ")

'''to search how many letters in
   Your name,so here I used
 dictionary
 method 'get()' to find letters
 in name
'''
name=input("enter your name ")
d={}
for letter in name:
    value= d.get(letter,0)+1
    d[letter]=value
print (d)

m={'maadhi':55}
print(m.get('maadhi'))
print(m.get('sivamukha',0)+1)

def up(username, password):
    if username!='maa':
        print("incorrect password")
        username=input("enter a username")
        password=input("enter a passwor")
        up(username, password)

    elif password!='maa ':
        print("incorrect password")
        username=input("enter a username")
        password=input("enter a password")
        up(username, password)


username=input (" username:")
password=input ("password:")
up(username, password)

h=0
def add(n):

    print(n)
    global h
    h+=n
    print (h)
    n+=1


    if n<=5:
        add(n)
add(1)

'''recursion'''
F=1
def fact(f):
    global F

    F*=f
    f+=1
    print (F)
    if f<=10:


        fact(f)
fact(1)

'''recursion factorial and addition of
First n number'''
def facto(n):

    if n==1:
        return 1
    else:
        return n*facto(n-1)

for x in range (1,10):

  print(facto(x))

def sumofdigits(num):
    if num==1:
        return 1
    else:
        rem= num%10
        no= num//10

        return rem+sumofdigits(no)
sumofdigits(12345)