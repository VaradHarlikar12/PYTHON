class Student():
    college_name=("latthe college")
    name="anonymous"#class attri
    #paramtilized construtor
    def __init__(self,name,marks):
        self.name=name #obj attri>class attri
        self.marks=marks
        print("adding an new student")
    def welcome(self):
        print("welcome student",self.name)

    def get_marks(self):
        return self.marks

s1=Student("varad",97)
print(s1.name)
print(s1.marks)
print(s1.welcome())
print(s1.get_marks())
s2=Student("ayush",99)
print(s2.name)
print(s2.marks)
print(s2.college_name)
print(s2.welcome())
print(s2.get_marks())

#decorator
class school:
@staticmethod
def method():
    print("hello")
    