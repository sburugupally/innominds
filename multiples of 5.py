#Find the sum of all the multiples of 3 or 5 below 1000
num=int(input("enter the number:"))
sum=0
for i in range(1,1000):
    if(i%num==0):
        sum+=i
        print(sum)
