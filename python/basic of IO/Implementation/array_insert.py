n,q=map(int,input().split())
A=list(map(int,input().split()))
for i in range(q):
    a,b,c=map(int,input().split())
    if a==1:
        A[b]=c
    elif a==2:
        if c-b<=len(A)-1:
            print(sum(A[b:c+1]))
        else:
            print(-1)

