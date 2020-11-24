#https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/can-you-solve-it/
for t in range(int(input())):
    n=int(input())
    A=list(map(int,input().split()))
    x=[A[i]+i for i in range(n)]
    y=[A[j]-j for j in range(n)]
    print(max(max(x)-min(x),max(y)-min(y)))
