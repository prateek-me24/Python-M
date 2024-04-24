##  1.

start_char = ord('A')
for i in range(4,0,-1):
    for k in range(4,i,-1):
        print(" ", end=' ')
    for j in range(i):
        print(chr(start_char +j), end=" ")
    print('')
    start_char+=1

print('\n\n')

##  2.

start_char = ord('A')
for i in range(4,0,-1):
    for k in range(4,i,-1):
        print(" ", end=' ')
    for j in range(i):
        print(chr(start_char +j), end=" ")
    print('')
    
print('\n\n')

##  3.

start_char = ord('A')
num = 10
for i in range(4,0,-1):
    if(i%2==0):
        for k in range(4,i,-1):
            print(" ", end=' ')
        for j in range(i):
            print(chr(start_char +j), end=" ")
        print('')
        start_char+=1

    else:
        n = num
        for k in range(4,i,-1):
            print(" ", end=' ')
        for j in range(i):
            print(n, end=' ')
            n*=10
        print('')
        num *= 10


print('\n\n')

##  4.


start_char = ord('Z')
for i in range(1,4):
    for j in range(i-1):
        print(' ', end=' ')
    for k in range(i,4):
        print(chr(start_char), end=' ')
        start_char-=1
    print('')
    

print('\n\n')

##  5.


for i in range(1,6):
    for j in range(i-1):
        print(' ',end=' ')
    for k in range(i,6):
        if(i==1 or i==5 or k==5 or k==i):
            print('*', end=' ')
        else:
            print(' ',end=' ')
    print('')
    

print('\n\n')

##  6.


for i in range(1,6):
    for k in range(6-i):
        # print('*',end=' ')
        if(i==1 or i==5 or k==0 or k==6-i-1):
            print('*', end=' ')
        else:
            print(' ',end=' ')
    print('')
    

print('\n\n')