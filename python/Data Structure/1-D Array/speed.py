#https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/speed-7/
for _ in range(int(input())):
    n=int(input())
    A=[int(x) for x in input().split()]
    cnt=1
    main=A[0]
    for i in range(1,n):
        if A[i]<=main:
            cnt+=1
            main=A[i]
    print(cnt)
