l=int(input())
for _ in range(int(input())):
    w,h=map(int,input().split())
    if w>=l and h>=l:
        if w==h:
            print('ACCEPTED')
        else:
            print('CROP IT')
    else:
        print("UPLOAD ANOTHER")
