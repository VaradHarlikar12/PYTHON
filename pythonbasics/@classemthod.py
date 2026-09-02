class Person:
    name="anonymous"
    @classmethod
    def change_name(cls,name):
        cls.name=name

p1=Person
p1.change_name("varad")
print(p1.name)

class Student:
    def __init__(self,phy,chem,maths):
        self.chem=chem
        self.phy=phy
        self.maths=maths

    @property
    def percentage(self):
       return str((self.phy + self.chem + self.maths) / 3) + "%"


s1=Student(98,99,92)
print(s1.percentage)
s1.phy=86
print(s1.percentage)
