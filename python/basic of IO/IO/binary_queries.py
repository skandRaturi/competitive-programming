

X=list(map(int,input().split(" ")))
N=list(map(int,input().split(" ")))


def binary_conversion(x):
    converted=0
    y=x[::-1]
    for i in range(len(y)):
        a=y[i]*(2**i)
        converted+=a
    return converted



for i in range(X[1]):
    Q=list(map(int,input().split(' ')))
    if Q[0]==1:
        if N[Q[1]-1]==1:
            N[Q[1]-1]=0
        else:
            N[Q[1]-1]=1
    else:
        A=N[Q[1]-1:Q[2]]
        e=binary_conversion(A)
        if e%2==0:
            print('EVEN')
        else:
            print('ODD')
        
        
