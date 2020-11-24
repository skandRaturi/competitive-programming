N=int(input())

x=list(map(int,input().split()))

Q=int(input())

a=[]

if 1<=N and N<=10**5 and Q>=1 and Q<=10**5:
    
    for i in range(Q):
        y=int(input())
        if x.count(y)==0:
            a.append("NOT PRESENT")
        else:
            a.append(x.count(y))
    for b in a:
        print(b)
