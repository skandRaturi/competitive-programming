X=int(input())
A=list(map(int,input().split()))
C=[]
for i in range(X):
    count=0
    for j in range(i+1,X):
        if A[i]>A[j] or A[i]==A[j]:
            count+=1
        else:
            break
    if count==X-i-1:
        C.append(str(A[i]))
print(' '.join(C))
