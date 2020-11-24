x=int(input())
a=list(map(int,input().split()))
ans=1
mod=(10**9)+7
for _ in a:
    ans*=_
print(ans%mod)
