x=int(input())
for i in range(x):
    N=int(input())
    a=N%12
    if a==0:
        print(N-11, 'WS')
    elif a==1:
        print(N+11, 'WS')
    elif a==2:
        print(N+9, 'MS')
    elif a==3:
        print(N+7, 'AS')
    elif a==4:
        print(N+5, 'AS')
    elif a==5:
        print(N+3, 'MS')
    elif a==6:
        print(N+1, 'WS')
    elif a==7:
        print(N-1, 'WS')
    elif a==8:
        print(N-3, 'MS')
    elif a==9:
        print(N-5, 'AS')
    elif a==10:
        print(N-7, 'AS')
    elif a==11:
        print(N-9, 'MS')
        
    
