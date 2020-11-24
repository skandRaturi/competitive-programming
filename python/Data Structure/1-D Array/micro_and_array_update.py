T=int(input())
for j in range(T):
    N,K=map(int,input().split())
    A=sorted(list(map(int, input().split())))
    if A[0]<K:
        print(K-A[0])
    else:
        print(0)
