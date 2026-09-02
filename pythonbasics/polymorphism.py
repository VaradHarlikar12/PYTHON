#dunder function uses
# polymorphism means one thing has multiple forms according to context
# polymorphism:overloading operators
print(1 + 2)  # 3 adding
print("varad" + "op")  # concatenate
print([1, 2, 3, ] + [4, 5, 6])  # merge


class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def shownumber(self):
        print(self.real, "i+", self.img, "j")

    def __add__(self,num2):
        newreal = self.real + num2.real
        newimg = self.img + num2.img
        return Complex(newreal, newimg)


num1 = Complex(1, 3)
num1.shownumber()

num2 = Complex(4, 6)
num2.shownumber()

num3=Complex(3, 6)
num3.shownumber()
num = num1 + num2
num.shownumber()

class Circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 22/7*self.radius**2

    def peri(self):
        return 2*22/7*self.radius

c1=Circle(2)
print(c1.radius)
print(c1.area())
print(c1.peri())


class enrollment:
    def __init__(self, name, age, marks):
        self.name = name
        self.age  = age
        self.marks = marks

    def mark(self):
        if(self.marks>=90):
            print("admission approved")
        else:
            print("admission denied")

std1=enrollment("varad",19,91)
std1.mark()
