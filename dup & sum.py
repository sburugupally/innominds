#Remove duplicates from the list: a=[1,2,3,2,3,4,1,,3,4]
"""
a=[1,2,3,2,3,4,1,3,4]
duplicates= set()
different= []
for i in a:
    if i not in duplicates:
        different.append(i)
        duplicates.add(i)
print(duplicates)

#Remove duplicates from the list: a=[1,2,3,2,3,4,1,,3,4]
dup = [1,2,3,2,3,4,1,3,4]
def delete(dup):
    list = []
    for num in dup:
        if num not in list:
            list.append(num)
    return list
print(delete(dup))


# l=['1','2','3'] get the sum of the list
l=['1','2','3']
sum=0
for i in l:
    sum=sum+int(i)
print(sum)
"""


#l1=[1,2,3,4] l2=[5,6,7,8] sum of two lists
l1=[1,2,3,4] ;   l2=[5,6,7,8]
l3=[(x+y) for x,y in zip(l1,l2)]
print(l3)




