###
"""
l=[1,2,3,4,5]
#printing the last element in list
print("l[-1]= ", l[-1])
# reversing the list using slicing#
print("l[ : : -1]= ", l[ : : -1])
#reversing the list using user defined#
l.reverse()
print(l)
# splitiung the string to letters#
str="shanno"
str=list(str)
print(str)
#spliting  the string to words#
str="she is good and beautifull"
print(str.split())

str="2017-04-11T15:07:59"
list=str.split('T')
print(list)

d={1:'hjdvj',2:'hyfuf',3:'jgk',4:'hsjks'}
print(d.keys())
print(d.values())
print(d.get(3))

print(list(range(4,10,2)))
print(list(range(2,-14,-2)))

l=[1,2,3,4]
l.append(6)
print(l)
l.extend([6767]) keys = ['a', 'b', 'c']
>>> values = [1, 2, 3]
>>> dictionary = dict(zip(keys, values))
>>> print(dictionary)
print(l)

"""
def func(*args):
    for i in args:
        print(i)
    func(2,3,4,6,7,9,9)

dict{[1,2],[3,4],[5,6]}
