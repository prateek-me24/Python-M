
##  1.

for i in range(4,0,-1):
    for j in range (i):
        print('*',end='')
    print("")

print('\n\n')
##  2.

n=10
for i in range(1,4):
    for j in range(0,i):
        print(n, end=' ')
        n+=1
    print('')

print('\n\n')
##  3.

for i in range(4):
    for j in range(i+1):
        print(chr(ord('d') -j), end="")
    print('')

print('\n\n')
##  4.


for i in range(1,5):
    for j in range(10,(10+i)):
        print(j, end=' ')
    print('')

print('\n\n')
##  5.

for i in range(4):
    for j in range(i+1):
        print(chr(ord('a') +j), end="")
    print('')

print('\n\n')
##  6.

for i in range(4,0,-1):
    for j in range(i):
        print(chr(ord('D') -j), end="")
    print('')

print('\n\n')
##  7.

for i in range(1, 5 + 1):
    for j in range(1, i + 1):
        if(j%2==0):
            print(2, end='')
        else:
            print(1,end='') 
    print('')

print('\n\n')
##  8.

start_letter = ord('F')
for i in range(4):
    for j in range(i+1):
        print(chr(start_letter), end="")
        start_letter+=2
    print('')

print('\n\n')
