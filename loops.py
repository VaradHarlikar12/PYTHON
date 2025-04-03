#1 to 100
add_one=1
while add_one<=100:
    print(add_one)
    add_one+=1
#100 to 1
sub_one=100
while sub_one>=1:
    print(sub_one)
    sub_one-=1

n =int(input("enter an value"))
i=1
while i<=10:
    print(n*i)
    i+=1
#
nums=[12,32,53,34,75,78,27,82,94,64]
idx=0
num=(12,12,32,48,42,1,92,34,5,35)

while idx<len(nums):
    print(nums[idx])
    idx += 1
#FINDING AN NUMBER
i=0
x=32
while i<len(num):
    if(num[i]==x):
       print("FOUND AT IDX:",i)
       i+=1