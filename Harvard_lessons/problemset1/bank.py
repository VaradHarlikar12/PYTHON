greeting=input("How are u doing? ")

def Greetback(x):
    if x=="Hello" or x=="HELLO" or x=="hello":
        print("$0")
    elif x.startswith("H"):
        print("$20")
    else:
        print("$100")


Greetback(greeting)
