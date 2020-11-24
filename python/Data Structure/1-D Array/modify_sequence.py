https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/modify-sequence/
n=int(input())
s=0
A=list(map(int,input().split()))
for i in range(n):
    s+=A[i]*(10**i)
if s%11==0:
    print("YES")
else:
    print("NO")
