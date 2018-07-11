#Take some single digit numbers from the user and findout min, maximum, sum, average
def minmaxsumavg():
    lst= [1,2,3,4,5]
    min = max = sum = lst[0]
    i=0
    while i < len(lst):
        if lst[i] > max:
            max = lst[i]
        if lst[i] < min:
            min = lst[i]
        sum += lst[i]
        i += 1
    avg=sum/len(lst)
    print(max,min,sum,avg)
    return min, max, sum,avg

min,max,sum,avg = minmaxsumavg()
