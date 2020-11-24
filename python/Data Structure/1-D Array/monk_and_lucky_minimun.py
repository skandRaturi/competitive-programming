#https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/monk-and-lucky-minimum-3/
from sys import stdin
for _ in range(int(input())):
    n=int(stdin.readline())
    A=list(map(int,stdin.readline().split()))
    if A.count(min(A))%2==0:
        print("Unlucky")
    else:
        print("Lucky")
