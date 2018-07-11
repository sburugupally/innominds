"""
#Print the first 100 odd numbers
for i in range(0,100):
    if(i%2!=0):
        print("print the odd number:")
        print(i)

"""
#Determine the factors of a number entered  by the user
num=int(input("enter the number:"))
for i in range(1,num + 1):
    if(num%i == 0):
        print("print the factor:", i)