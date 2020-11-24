n=int(input())
x=list(map(int,input().split()))
count=1
for _ in range(1,n):
    if x[_]>=x[_-1]:
        continue
    else:
        count+=1
print(count)
