#https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/help-jarvis-8a39566efor t in range(int(input())):
    A=[int(x) for x in input()]
    if len(set(A))==len(A):
        if max(A)-min(A)==len(A)-1:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")/
