#https://www.hackerearth.com/practice/basic-programming/operators/basics-of-operators/practice-problems/algorithm/birthday-party-12/
for i in range(int(input())):
    n,m=map(int,input().split())
    if m%n==0:
        print("Yes")
    else:
        print("No")
