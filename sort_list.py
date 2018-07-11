#l=['a','A','b','B','d','D','c','C'] sort the list properly
l = ['a','A','b','B','d','D','c','C']
def sorting(l):
    for i in range(0,len(l)):
        for j in range(0,len(l)-1):
            if l[j]>l[j+1]:
                temp=l[j+1]
                l[j+1]=l[j]
                l[j]=temp
    return l
print(sorting(l))