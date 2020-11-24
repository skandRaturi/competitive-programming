x=input()
if len(x)==10:
    s=0
    for i in range(1,11):
        s+=i*int(x[i-1])
    if s%11==0:
        print('Legal ISBN')
    else:
        print('Illegal ISBN')
else:
    print('Illegal ISBN')
