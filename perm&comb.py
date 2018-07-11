#input fun('abc') output: [[],][a],[b],[c],[a,b],[b,c],[c,a],[a,b,c]


def fun(str):
    new=[]
    lst=list(str)
for i in range (0,len(lst+1):
    comb= combinations(list(str),i)
    for i in (comb):
        new.append(list(i))
    return new
data=input("enter string")
print(fun(data))
