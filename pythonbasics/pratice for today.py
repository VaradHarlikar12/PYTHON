nums=[12,42,53,75,35,65,29,91,17,37]
i=0
x=int(input("enter an value to search from list"))
while i<len(nums):
    if(nums[i]==x):
        print("found")
        break
    else:
        i+=1
        print("finding...")

print("end")
a=0
while a<=5:
    if(a==3):
        a+=1
        continue
    print(a)
    a+=1
n=7
sum=0
for sum_n_no in range(1,n+1):
    sum+=sum_n_no
    print("total sum",sum)
