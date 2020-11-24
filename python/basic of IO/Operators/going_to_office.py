#https://www.hackerearth.com/practice/basic-programming/operators/basics-of-operators/practice-problems/algorithm/going-to-office-e2ef3feb/
D=int(input())
oc,of,od=map(int,input().split())
cs,cb,cm,cd=map(int,input().split())
co=oc+(D-of)*od
cc=cb+(D//cs)*cm+(D*cd)
if co<=cc:
    print("Online Taxi")
else:
    print("Classic Taxi")
