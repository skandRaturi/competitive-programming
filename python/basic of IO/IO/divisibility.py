n=int(input())
a=list(map(str,input().split()))
b=''
for i in range(n):
    b+=a[i][-1]
if int(b)%10==0:
    print('Yes')
else:
    print("No")
