#https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/only-even/


for i in range(int(input())):
    n=int(input())
    cnt=0
    a=input().split()
    for j in range(n):
        if int(a[j])%2==0:
            cnt+=(n-j)*(j+1)
    print(cnt)
