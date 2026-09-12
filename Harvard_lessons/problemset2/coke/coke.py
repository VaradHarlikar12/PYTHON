#In a file called coke.py, implement a program that prompts the user to insert a coin,
#one at a time, each time informing the user of the amount due. Once the user has inputted at least 50 cents,
#output how many cents in change the user is owed. Assume that the user will only input integers,
#and ignore any integer that isn’t an accepted denomination.

def Coke():
    Amount_due=50
    while Amount_due > 0:
        print("Amount due",Amount_due)
        coin=int(input("Insert Amount:"))
        if(coin == 25 or coin == 10 or coin == 5):
            Amount_due = Amount_due - coin
    print("Change owed",abs(Amount_due))

Coke()

