for a in range(int(input())):
    j=int(input())
    for i in range(1,j+1):
        j-=1
        print(("*"*i)+("#"*j*2)+("*"*i))
    print("")
