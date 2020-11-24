s=0
for i in range(int(input())):
    r,x=map(int,input().split())
    b=100*x
    a=22*(r*2)/7
    if b>=a:
        s+=1
print(s)
