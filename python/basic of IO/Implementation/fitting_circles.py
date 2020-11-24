for i in range(int(input())):
    A=input().split()
    if int(A[0])>=int(A[1]):
        print(int(A[0])//int(A[1]))
    else:
        print(int(A[1])//int(A[0]))
