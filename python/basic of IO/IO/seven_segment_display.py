A={"0":6,"1":2,"2":5,"3":5,"4":4,"5":5,"6":6,"7":3,"8":7,"9":6}
for i in range(int(input())):
    a=input()
    n=0
    for j in a:
        n+=A[j]
    if n%2==0:
        p="1"*(n//2)
    else:
        p='7'+'1'*((n//2)-1)
    print(p)
