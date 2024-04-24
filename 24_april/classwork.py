
num = 1
for i in range(1,4):
    for j in range(1,i+1):
        print(num, end=' ')
        num*=2
    print('')

print('\n')
num=17
for i in range(3):
    for j in range(0,i+1):
        print (num, end=' ')
        num+=2
    print('')


print('\n')

for i in range(1,5):
    for j in range(1,i):
        print(' ', end=' ')
    for k in range(i,5):
        print('*', end=' ')
    print("")

for i in range(1,5):
    for j in range(1,i):
        print(" ", end=' ')
    for k in range(1,6-i):
        print(k, end=' ')
    print('')

print('\n')

n=1
for i in range(1,5):
    for j in range(1,i):
        print(" ", end=' ')
    for k in range(1,6-i):
        print(n, end=' ')
        n+=1
    print('')

print('\n')

for i in range(1,5):
    for j in range(1,i):
        print(" ", end=' ')
    for k in range(1,6-i):
        if(i%2==0):
            print('#', end=' ')
        else:
            print('$', end=' ')
    print('')

    
print('\n')

n=4 
for i in range(1,5):
    for j in range(1,i):
        print(" ", end=' ')
    for k in range(1,6-i):
        print(n, end=' ')
        n+=2 
    print('')


print('\n')

for i in range(1,6):
    for j in range(1,i+1):
        if(i<3 or i==5 or i==j or j==1):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print('')