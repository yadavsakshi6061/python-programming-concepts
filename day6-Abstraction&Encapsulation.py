"""
Abstraction
Hiding the implementation details of class and only
showing the essential feature to the user
"""
class Car:
    def __init__(self):
        self.acc =False
        self.brk =False
        self.clutch = False

    def start(self):
        self.acc =True
        self.acc =True
        print("car started")

car1 = Car()
car1.start()
"""
Encapsulation
Wrapping data and function into  single unit(obj)
"""

#practice
"""
create Account class with 2 attributes - balance and account no 
create method for debit,credit and printing the balance 
"""

class Account:
    balance = 5000
    account_no = 123

    def __init__(self):
        pass

    @staticmethod
    def debit(): #sub
        acc = int(input("Enter the debit amt:"))
        Account.balance -= acc
        print(f"Debited {acc} from account. Updated balance: {Account.balance}")


    @staticmethod
    def credit(): #add
        acc= int(input("enter your  credit amount:"))
        Account.balance += acc
        print(f"Credited {acc} to account. Updated balance: {Account.balance}") #{} in python work as an place holder for var

acc = Account()
acc.debit()
acc.credit()

#other EX2

class Acc:
    def __init__(self,bal,acc_no):
        self.bal = bal
        self.acc_no = acc_no

    def D(self,amt):
        self.bal -= amt
        print("the D amt is :",amt)
        print("Total:",self.get_bal())


    def C(self,amt):
        self.bal+=amt
        print("the C amm is :",amt)
        print("Total:",self.get_bal())


    def get_bal(self):
        return self.bal


acc1 = Acc(5000,1)
acc1.D(1000)
acc1.C(500)
