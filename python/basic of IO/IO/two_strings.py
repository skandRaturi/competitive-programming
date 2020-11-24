for _ in range(int(input())):
    a,b=map(str,input().split())
    a=sorted(a)
    b=sorted(b)
    if a==b:
        print("YES")
    else:
        print("NO")
