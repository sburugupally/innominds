#take a number from the user and check whether it is prime
num=int(input("enter the number:"))
if(num>1):
    for i in range(2,num):
        if(num%i)==0:
            print("num is not prime")
        else:
            print("num prime number")