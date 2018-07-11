#find out the perfect numbers

"""
num=int(input("enter the number:"))
sum=0
for i in range(1,num):
    if(num%i== 0):
        sum= sum+i
if(sum==num):
    print("number is perfect")
else:
    print("number is not perfect")

"""
#find out the perfect numbers in the given range
min=int(input("enter the number1:"))
max=int(input("enter the number1"))
for num in range(min,max-1):
    sum=0
    for i in range(1,num-1):
        if(num%i== 0):
            sum=sum+i
    if(sum==num):
        print(num)