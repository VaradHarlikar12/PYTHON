#abstract
#it is basicially hidding details and showing the main part only
class Car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False
    def start(self):
        self.clutch=True
        self.acc=True
        print("CAR started........")

car1=Car()
car1.start()

class Account:
    def __init__(self,bal,acc,bank):
        self.balance=bal
        self.account_no=acc
        self.bank=bank

    def debit(self,amount):
        self.balance-=amount
        print("Rs.",amount,"was debited")
        print("total balance=",self.get_newbalance())
    def credit(self,amount):
        self.balance+=amount
        print("Rs.",amount,"was credited")

    def get_newbalance(self):
        return self.balance


acc1=Account(90008,98765432,"icic")
acc2=Account(90007,98765443,"sfc")

acc1.debit(1000)
acc1.credit(2000)
print(acc1.balance)
print(acc2.balance)
acc2.credit(1000)
acc2.debit(2987)
