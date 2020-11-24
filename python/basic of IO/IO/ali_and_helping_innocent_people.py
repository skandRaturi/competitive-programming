x=input()
if (int(x[0])+int(x[1]))%2==0 and x[2] not in 'AEIOUY' and (int(x[3])+int(x[4]))%2==0 and (int(x[4])+int(x[5]))%2==0 and x[6]=='-' and (int(x[7])+int(x[8]))%2==0:
    print('valid')
else:
    print('invalid')
