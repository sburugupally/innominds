"""
#take a string from the user and check contains atleast one digit or not?
str=input("enter the string:")
for ch in str:
    if (ch>='0' and ch<='9'):
        print("string is alphanumeric")
        break
else:
    print("string is not alphanumeric")




#take a string from the user and check contains atleast one alphabetic or not?
str=input("enter the string:")
for ch in str:
    if (ch>='a' and ch<='z'):
        print("string has atleast one letter")
        break
else:
    print("string doesnt have any letter")




#take a string from the user and check contains atleast one capital letter or not?
str=input("enter the string:")
for ch in str:
    if (ch>='A' and ch<='Z'):
        print("string has atleast one  capital letter")
        break
else:
    print("string doesnt have any capital letter")
"""


#take a string from the user and check contains atleast one small letter or not?
str=input("enter the string:")
for ch in str:
    if (ch>='a' and ch<='z'):
        print("string has atleast one small letter")
        break
else:
    print("string doesnt have any small letter")

