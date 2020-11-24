#https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/strange-game-1-7e758acb-1bff10f0/description/
from sys import stdin
for t in range(int(input())):
    n,k=map(int,stdin.readline().split())
    A=list(map(int,stdin.readline().split()))
    B=list(map(int,stdin.readline().split()))
    c=max(B)
    cnt=0
    for i in range(n):
        if A[i]<=c:
            cnt+=c-A[i]+1
    print(cnt*k)
