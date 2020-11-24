#https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/mark-the-answer-1/description/
from sys import stdin
n,x=map(int,input().split())
A=list(map(int,stdin.readline().split()))
cnt=0
m,i=-1,0
while m<1:
    if i<n:
        if A[i]<=x:
            cnt+=1
        else:
            m+=1
    else:
        break
    i+=1
print(cnt)
