class mnc:


    @staticmethod
    def salary (no1,no2):
        print ("salary is ",no1+no2)
mnc.salary(1,2)
#print (Ramu)

class bank:
    No_of_holiday=10

    @classmethod
    def info(cls,branch):
        print ("our",branch,"branch has ", cls.No_of_holiday,"holidays")
H=bank.info("Chennai" )
G=bank()
G.No_of_holiday

Ghjj



import sys
class customer:
    Bank="welcome to SBI "
    def __init__(self,name,accno,balance=500):
        self.name= name
        self.accno= accno
        self.balance= balance



    def deposit(self,amount):
        self.balance= self.balance+amount



    def withdraw(self, amount):

        if self.balance<amount:
            print ("insufficient balance")
        else:
            self.balance= self.balance-amount

print (customer.Bank)
name= input("what is your name?")
accno= int(input("enter your account number "))
Customer1= customer(name,accno)
while True:
    print ("enter your choice")
    print ("D- deposit,W- withdraw,S-stop")
    choice=input("enter your choice")
    if choice=='D':
        amount= int(input ("enter a amount to deposit"))
        Customer1.deposit(amount)
    elif choice=='W':
        amount= int(input ("enter a amount to withdraw"))
        Customer1.withdraw(amount)
    elif choice=='S':
        sys.exit()

'''Inheritance'''
'''has relationship '''
''' has -aggregation,
 Is-composition '''


class Enginee:
    mileage=20
    def __init__(self):
        self.petrol= True
        self.disel= False
        self.madhi= "here"
    def engineestart(self):
        print ("enginee smooth starting",self.petrol,self.disel,self.madhi)
class car(Enginee):
    def __init__(self,speed,price):
        super().__init__()

        self.foreign= Enginee()
        self.speed= speed
        self.price= price



    def drive(self):
        print(self.foreign.mileage)
        print (self.foreign.engineestart())
        print (self.disel)
        print (self.price)

car1= car(56,60)
print (car1.speed)
#car1.price= 56
#car1.speed=4000
#rint (car1.price,car1.speed)

''' Is relationship '''
''' Ramu is a human'''
'''child      parent relationship '''


class ReserveBank:
    def __init__(self):
        self.branch= "Chennai"
    def deposit (self):
        print ("today",self.branch,"branch huge money deposit")
class Sbi(ReserveBank):
    pass


Trichy=Sbi()
Trichy.deposit()

class VasanthaAndCo:
    J= 40
    def __init__(self):
        self.hq_offer=100

class VasanthCo_madurai(VasanthaAndCo):
    def __init__(self):
        super().__init__()
        self.bq_offer=50






F=VasanthCo_madurai()


H=F.hq_offer
#
print (H)
M=F.bq_offer
print (M)
print (F.J)

class parent:


    def play(self):
        print ("hello playing")


    @classmethod
    def working(cls):
        print("hello Im father")




class child(parent):
    @classmethod
    def baby(cls):
        super(child,cls).play(cls)
        super().working()



C1=child()
C1.baby()

'''operator overloading '''

class library:
    def __init__(self,improve,scific,comics):
        self.improve= improve
        self.scific=scific
        self.comics=comics


    def __add__(self,d):
        return self.improve+self.scific+self.comics+d.offer


class discount:
    def __init__(self,offer):
        self.offer=offer






Stud1=library (150,150,200)


Stud2=discount(100)

print (Stud1+Stud2)

'''method overloading '''
class test:
   def mark(self,no1,no2,no3):
      print ("hello")

   def mark(self,*no1):
      print (no1)
N=test()
N.mark(1,2,3,4)

'''construct overloading '''

class supermarket:
    def __init__(self, *no):
        self.no=no
    def total(self):
        return(self.no)







G=supermarket(1,2,3)
#G=supermarket(1,1,2)

G.total()

'''abstraction'''

from abc import *



class ancestors(ABC):

    @abstractmethod
    def house(self):
        print ("I will give you this house")
class dad(ancestors):
    #abstractmethod
    def house(self):
        print ("I will give this house to my son")




G="a"
H= globals()[G]
M=H()
M.house()



'''
Encapsulation

for attributes only
It's may be class attribute or object
attributes

1.  (Default) is  public

2.  _  ( protected) access same
            class and same inherit
                        class


3.  __  ( Private ) only within
                    class access


ex: _a= 10
Access private outside of class
     : Objname.__classname__attri
                    bute name


'''