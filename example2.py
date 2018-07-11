s1='shanno'
s2=s1[ : : -1]
print(s2)
if(s2 == s1):
    print("string is palidrome",s2)
else:
    print("string is not palidrome", s1)

num= 404
sum=0
n=num
while(n!=0):
 rev=num%10
 sum=sum*10+rev
 num=num/10
if(sum == n):
 print("number is palidrome",)
else:
  print("number is not palindrome")