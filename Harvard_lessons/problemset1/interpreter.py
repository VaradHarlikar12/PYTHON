expression=input("Enter your expression:-")
z
def Interpreter(expression):
    x, y, z=expression.split()
    x=int(x)
    z=int(z)
    if y == "+":
        answer = x+z
    elif y == "-" :
        answer = x-z
    elif y == "*" :
        answer = x*z
    elif y == "/" :
        answer = x/y

    print(f"{answer:.1f}")


Interpreter(expression)
