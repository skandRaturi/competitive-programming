#https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/snackdown-contest/
for _ in range(int(input())):
    n=int(input())
    a=[x for x in input().split()]
    b=[x for x in input().split()]
    a=a[1:]+b[1:]
    c={0}
    for i in a:
        c.add(i)
    if len(c)==n+1:
        print("YES")
    else:
        print("NO")
