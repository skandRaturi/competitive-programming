x=int(input())
s=input()
if "HH" in s:
    print("NO")
else:
    S=''
    for i in s:
        if i=="H":
            S+=i
        else:
            S+="B"
    print("YES")
    print(S)
