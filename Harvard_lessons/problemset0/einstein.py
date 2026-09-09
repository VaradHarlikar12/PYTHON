# implement a program in Python that prompts the user for mass as an integer (in kilograms)
# and then outputs the equivalent number of Joules as an integer.Assume that the user will input an integer.

def Einstein():
    mass=int(input("Enter an value for mass in kilograms "))
    c=300000000
    E=mass*c**2
    print(E)

Einstein()
