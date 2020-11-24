N=int(input())
if N>1 and N<=1000:
    A=[]
    for i in range(2,N+1):
        a=0
        for j in range(2,i):
            if i%j==0:
                a+=1
        if a==0:
            A.append(str(i))
    print(' '.join(A))
elif N==1:
    print(0)
