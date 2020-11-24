n=int(input())
A=list(map(int,input().split()))
cnt=0
for i in range(n):
    if A.count(A[i]+1)!=0:
        cnt+=A.count(A[i]+1)+A.count(A[i]+2)
    else:
        cnt+=A.count(A[i]+1)


print(cnt)
