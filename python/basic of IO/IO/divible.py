N=int(input())
A=input().split()
s=''
for i in range((N//2)):
    s+=A[i][0]
for i in range(N//2,N):
    s+=A[i][-1]
if int(s)%11==0:
    print("OUI")
else:
    print("NON")
