x=input()
A=[]
B=[]
for a in x:
	if int(a)%2==0:
		A.append(int(a))
	else:
		B.append(int(a))

c=0
d=0
for i in A:
	c+=i
for j in B:
	d+=j
print(c,d)
