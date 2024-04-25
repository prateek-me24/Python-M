## continue statement

for i  in range(1,10):
    if(i==3):
        continue
    print(i)

## prime numbers
#   6

num = int(input("Enter a number to check prime : "))
x=0
for i in range(2,num):
    if (num%i==0):
        x=1
        break

if(x==1):
    print('not a prime number')
else:
    print('prime number')


# List ( sequence )
# collection of multiple elements of different datatype
# Mutable
# element can be mutable or immutanle
# []
# update, delete, insert and  access based on index position

myList = [10,20,30.0,"hello"]
print(type(myList))

print(myList[3])

print(myList[-1])

print(myList[0:3])

print(myList[-1:-3:-1])

myList[0] = 90
print(myList[0])

myList[0:2] = ['A','B']
print(myList)




###   List Functions

myList.append("prateek")

myList.extend("yash")

myList.extend(["yash"])

x = myList.pop()  ##  remove last element and return

myList.pop(1)  ## specify index number

print(help(myList))  ##  for help

myList = [10,20,30.0,"hello",20]

myList.remove(20)  ## send specific value, removed from left side if multiple times it ccomes

del myList[0]


print(myList)

for i in myList:
    print(i)



testList = [10, "hie", 10.2, 30, True]

for i in testList:
    if(type(i) is int):
        print(i)



intList = []
for i in testList:
    if(type(i) is int and i%2==0):
        intList.append(i)

print(intList)




val = int(input('enter the number here : '))
usrList =[]
for i in range(2,val):
    if(val%i==0):
        usrList.append(i)

print(usrList)