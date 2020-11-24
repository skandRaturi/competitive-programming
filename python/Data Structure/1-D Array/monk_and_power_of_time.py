N=int(input())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
time=N
for _ in range(N):
    while x[_]!=y[_]:
        x.append(x[_])
        x.pop(_)
        time+=1
    else:
        continue
print(time)
    
