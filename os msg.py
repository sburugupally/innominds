# Show the below menu to the user until and until user select quit and display corresponding os message

'''
Menu:
1. windows
2. Linux
3. Mac
4. quit
'''
def windows():
    print(" welcome to windows")
def linux():
    print("welcome to linux")
def mac():
    print("welcome to mac")
def quit():
    print("quit")
num=int(input("enter the choice:"))
if(num==1):
   windows()
elif(num==2):
    linux()
elif(num==3):
    mac()
else:
    quit()
