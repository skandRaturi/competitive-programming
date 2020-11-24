T=int(input())
mod=(10**9)+7
for i in range(T):
    N=int(input())-1
    A=list(map(int,input().split()))
    charge=0
    count=2**N
    for j in range(N+1):
        if A[j]>count or A[j]==count:
            charge+=A[j]
        else:
            continue
    print(charge%mod)
