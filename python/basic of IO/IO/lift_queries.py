A=0
B=7
for _ in range(int(input())):
    n=int(input())    
    if abs(n-A)>abs(n-B):
        A=n
        print("A")
    elif abs(n-A)<abs(n-B):
        B=n
        print("B")
    elif abs(n-A)==abs(n-B):
        if n-A>0:
            A=n
            print("A")
        elif n-B>0:
            B=n
            print("B")
    
            
        
            
