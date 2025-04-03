def cal_sum(a,b):
    return a+b

sum=cal_sum(1029,397)
print(sum)
#declare;
#call;
#define

#avg of three number
def average(a,b,c):
    sum=a+b+c
    avg=sum/3
    print(avg)
average(89,93,85)

def no_argue(b,a=2):#if only one default is passed then it is written from end
    print(a+b)
    return a+b
no_argue(1)
heroes=["superman","spider_man","batman","ironman","captain_america"]
def print_len(list):
    print(len(list))

    print_len(heroes)
def print_list(list):
    for item in list:
        print(item,end=" ")

print_list(heroes)
