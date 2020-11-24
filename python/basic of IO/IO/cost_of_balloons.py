t=int(input())
for _ in range(t):
    g,p=map(int,input().split())
    n=int(input())
    s1=0
    s2=0
    for i in range(n):
        a,b=map(int,input().split())
        s1+=a
        s2+=b
    A=[]
    A.append(s1*g+s2*p)
    A.append(s1*p+s2*g)
    print(min(A))
