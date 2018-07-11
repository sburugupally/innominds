#take a string from the user and check contains only  special chars or not?
str=input("enter the string:")
for i in str:
    if (i>='0' and i<='9') or (i>='a' and i<='z'):
        print("string has no special character")
        break
    else:
        print("string has special character")
        break
