""""
#input: "google" print count of each character

string = "google"
if string == 'dfjh':
    exit()
else:
    char = input("Enter a character to count to count from above string: ")
    num = string.count(char)
    print("Total = ",num)
"""

#l=[1,2,3] just make it as a string.
list=[1,2,3]
for i in range(len(list)):
    list[i]=str(list[i])
print(','.join(list))