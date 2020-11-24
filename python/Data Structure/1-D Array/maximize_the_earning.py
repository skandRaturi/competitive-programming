#https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/maximize-the-earning-137963bc-323025a6/
for t in range(int(input())):
    n,r=map(int,input().split())
    A=list(map(int,input().split()))
    cnt=1
    m=A[0]
    for i in range(1,n):
        if m<A[i]:
            cnt+=1
            m=A[i]
    print(r*cnt)
