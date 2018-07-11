#take a string from the user and check contains only  alphabets or not?
str=input("enter the string:")
for i in str:
    if (i>='a' and i<='z'):
        print("string is alphabetic")
    else:
        print("string is not alphabetic")
