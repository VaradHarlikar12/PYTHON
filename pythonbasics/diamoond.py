class A:
    def display(self):
        print("display from class A")


class B(A):
# def display(self):
#  print("display from class B")
    pass

class C(A):
    # def display(self):
    #     print("hi from class C")
    pass
class D(B, C):
    pass
    # def display(self):
    #     print("display from class D")


d1 = D()
d1.display()
