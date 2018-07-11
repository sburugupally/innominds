#Play a number guessing game (User enters a guess, you print YES or Higher or Lower)
i=100
num=int(input("enter the number between 1 to 30:"))
if(num== i):
    print("yes")
elif(num <= i):
    print("lower")
else:
    print("higher")
