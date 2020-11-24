x=int(input())
A=list(map(int,input().split(' ')))
B=list(map(int,input().split(' ')))
C=[]



for i in range(x):
    C.append(str(A[i]+B[i]))


    
print(' '.join(C))
