#https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/range-query-2/
n,q=map(int,input().split())
A=input().split()
for i in range(q):
    a=input().split()
    if a[0]=='1':
        if A[int(a[1])-1]=="0":
            A[int(a[1])-1]="1"
        else:
            A[int(a[1])-1]="0"
    else:
        if A[int(a[2])-1]=='1':
            print("ODD")
        else:
            print("EVEN")
