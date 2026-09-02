
def multi_table():
    n=float(input('enter an number for table : '))
    for i in range(1,11):
        table=n*i
        print(n," x ",i," = ",table)
multi_table()
def odd_even():
    n=int(input("enter an number:"))
    if(n%2==0):
        print("even")
    else:
        print("odd")
odd_even()
def usd_inr():
    inr=int(input("enter an inr value:"))
    usd=inr*83
    print("inr value:",inr,"usd value",usd)
usd_inr()
