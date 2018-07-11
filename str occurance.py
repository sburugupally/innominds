#findout third occurance of given substring
str="**she is playing in the garden**"
substr="*"
"""
def nth_cha(str,substr,n):
    n=0
    pos=-1
    for x in range(n):
        pos=str.find(substr,pos+1)
        if(pos==-1):
            return None
    return pos
    

substr=nth_cha(str,substr,n)

"""
def find_nth(str,substr,n):
    i=0
    while (n>=0):
       n=-1
       i=str.find(substr,i+1)
    print(i)
    return i
