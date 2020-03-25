#class5
a=int(input())

s = 'abcdefghijklmnopqrstuvwxyz'

for i in range(a):
    for j in range(a,i+1,-1):
        print('--', end = '')
    for j in range(i+1):
        if j!=i:
            print('{}-'.format(s[a-j-1]),end = '')
        else:
            print('{}'.format(s[a-j-1]),end = '')
    for j in range(a-i,a):
        print('-{}'.format(s[j]),end = '')
    for j in range(a,i+1,-1):
        print('--', end = '')
    print()
for i in range(a-1,0,-1):
    for j in range(a,i,-1):
        print('--', end = '')
    for j in range(i):
        if j!=i-1:
            print('{}-'.format(s[a-j-1]),end = '')
        else:
            print('{}'.format(s[a-j-1]),end = '')
    for j in range(a-1,a-i,-1):
        print('-{}'.format(s[j]),end = '')
    for j in range(i,a):
        print('--', end = '')
    print()
