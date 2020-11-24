for i in range(int(input())):
    sh,sm,eh,em=map(int,input().split())
    if em<sm:
        sh+=1
        print('%d %d' %(eh-sh,60-sm+em))
    else:
        print("%d %d" %(eh-sh,em-sm))
