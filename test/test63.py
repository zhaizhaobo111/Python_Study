a,b=map(int,input())
len=0
for i in range(a-1,b+1):
    m=i%10
    n=i/10
    if m%2==0 or n%2==0:
        len+=1
print(len)
