#Given an age, figure out whether someone's a baby, toddler, child, teenager, adult or old codger.
age=int(input("enter the age:"))
if(age<2):
    print("baby")
elif(age<3):
    print("toddler")
elif(age>=6 and age<=11):
    print("child")
elif(age>=11 and age<=18):
    print("teenager")
elif(age>=18 and age<=50):
    print("adult")
else:
    print("old codger")