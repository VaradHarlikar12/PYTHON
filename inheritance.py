class Car:

    @staticmethod
    def start():
        print("car has started...")

    @staticmethod
    def stop():
        print("car has stopped...")

class Toyota(Car):
    def __init__(self,brand):
       self.brand = brand

class Fortuner(Toyota):
    def __init__(self,type):
        self.type = type


c1=Fortuner("petrol","toyota")
c1.start()
c1.brand
class A:
    varA="WELCOME TO CLASS A"

class B:
    varB="WELCOME TO CLASS B"

class C(A,B):
    varC="WELCOME TO CLASS C"

c1=C()
print(c1.varC)
print(c1.varB)
print(c1.varA)
