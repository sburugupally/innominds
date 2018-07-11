
"""
#l=[10,20,30,[40,50,60],70,[80,90,20]] convert this  list to single dimensional list
l=[10,20,30,[40,50,60],70,[80,90,20]]
new_list=[]
for i in range(len(l)):
    if type(l[i]) is type(10):
        new_list.append(l[i])
    else:
        new_list.extend(l[i])
print(new_list)

"""
#l=[1,2,3,[4,5,6],7[8,9,1]] for single dimensional list
l= [1,2,3,[4,5,6],7[8,9,1]]
new_list=[]
for i in range(len(l)):
    if type(l[i]) is type(1):
        new_list.append(l[i])
    else:
        new_list.extend(l[i])
print(new_list)