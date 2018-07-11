# WAP to find union and intersection of lists.
"""
l1=[1,2,3,4]
l2=[5,6,7,8]
def union(l1,l2):
    return  list(set(l1) | set(l2))
def intersection(l1,l2):
    return list(set(l1) & set(l2))
print(union(l1,l2))
print(intersection(l1,l2))
"""
#another method

lst1 = []
num =int(input("Enter size of list 1:"))
for i in range(num):
    n =int(input("Enter any number:"))
    lst1.append(n)

lst2 = []
num2 = int(input("Enter size of list 2:"))
for i in range(num2):
    n1=int(input("Enter any number:"))
    lst2.append(n1)

union = list(set().union(lst1, lst2))
intersection=list(set.intersection(lst1,lst2))
print("union of lists", union)
print("intersection of lists",intersection)
