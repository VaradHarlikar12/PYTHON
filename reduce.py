from functools import reduce
no=[1,2,3,4,5]

def mysum(x,y):
    return x+y

sum=reduce(mysum, no)

print(sum)
