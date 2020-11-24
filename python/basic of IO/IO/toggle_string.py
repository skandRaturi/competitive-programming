a='abcdefghijklmnopqrstuvwxyz'
b=a.upper()
s=list(input())
for i in range(len(s)):
    if s[i] in a:
        s[i]=s[i].upper()
    elif s[i] in b:
        s[i]=s[i].lower()
print(''.join(s))
