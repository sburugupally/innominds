#write a program to chek given substring is there in actual string or not? (search should be case insensitive)
str="she is very good"
substr="she"
if substr in str:
    print("substring found")
else:
    print("substring not found")

#take a number from the user and check whether even or odd
num=int(input("enter the number:"))
if(num%2==0):
    print("num is even",num)
else:
    print("num is odd")


#take a number from the user and check whether it is prime
num=int(input("enter the number:"))
if(num>1):
    for i in range(2,num):
        if(num%i)==0:
            print("num is not prime")
        else:
            print("num prime number")
