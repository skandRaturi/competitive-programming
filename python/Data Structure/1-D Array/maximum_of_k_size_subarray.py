#https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/maximum-of-k-size-subarrays-deque/description/
from sys import stdin
n,k=map(int,stdin.readline().split())
A=list(map(int,stdin.readline().split()))
B=[]
for i in range(n-k+1):
    B.append(str(max(A[i:k+i])))
print(" ".join(B))    
