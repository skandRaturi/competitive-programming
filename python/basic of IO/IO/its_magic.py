n=int(input())
a=list(map(int,input().split()))
s=sum(a)
x=9999999994
y=0
for i in range(n):
    if (s-a[i])%7==0:
        if a[i]<=x:
            x=a[i]
        else:
            y+=1
if y==n:
    print(-1)
else:
    print(a.index(x))
