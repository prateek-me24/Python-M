##  1.

name = input("Enter your name : ")

print("Hello, ",name)


## 2.

a=-5
b=10

if((a+b)>0):
    print('positive')
else:
    print('negative')



##  3.

num = 23

while True:
    guess = int(input("Enter number here : "))

    if(guess == num):
        print('Correct')
        break
    else:
        print('Not matched, Try again!')




##  4.

firstName = input("Enter your first name : ")
lastName = input("Enter your last name : ")

wholeName = firstName +"."+ lastName

print(wholeName)



##  5.


value = input("Enter anything here : ")

toogle_str = ""
for chr in value:
    if chr.islower():
        toogle_str+=chr.upper()
    elif chr.isupper():
        toogle_str+=chr.lower()
    else:
        toogle_str+=chr
print(toogle_str)



##  6.


myList = [1,2,3,4,5,6]

sum = 0
multiply = 1

for i in myList:
    sum+=i
    multiply*=i

print("sum of my list : ", sum)
print("multiply of my list : ", multiply)



##  7.

x=89
a = [78,56,23,"hello",10]
res = 0

for i in a:
    if(i==x):
        res = 1
        break

if(res == 1):
    print('true')
else:
    print('false')



##  8.

a = [1,2,3,4,5,6]

b = [9,8,7,6,54,23]
res = 0
for i in a:
    for j in b:
        if(i==j):
            res = 1
            break

if(res == 1):
    print('true')
else:
    print('false')



##  9.

myList = [5,8,3]

for i in myList:
    for j in range(i):
        print("*", end=' ')
    print('')



##  10.

hundred_meters = ['Vikay','John','Kumar','Rajesh','Malar','Vaihai']
two_hundred_meters = ['Vetry','Petter','Priyanka','Kumar','Malar']

##  solve a.
print("Participate only 100 meters : ")
for i in hundred_meters:
    if(i not in two_hundred_meters):
        print(i)

print('\n\n\n')


##  solve b.
print("Participate only 200 meters : ")
for i in two_hundred_meters:
    if(i not in hundred_meters):
        print(i)

print('\n\n\n')


##  solve c.
print("Participate both 100 and 200 meters : ")
for i in hundred_meters:
    if(i in two_hundred_meters):
        print(i)

print('\n\n\n')



##  solve d.
print("Participate only one meters : ")
for i in hundred_meters:
    if(i not in two_hundred_meters):
        print(i)

for i in two_hundred_meters:
    if(i not in hundred_meters):
        print(i)

print('\n\n\n')



##  11.


List = [5,8,4,18,8,55,6,8,3,18,5,3,44]

check = []
duplicate = []
for i in List:
    if i in check and i not in duplicate:
        duplicate.append(i)
    else:
        check.append(i)

print("duplicate numbers are : ",duplicate)



##  12.


List = ["cat","tiger","lion", "zebra" , "crocodile", "snack"]

lstlen = len(List)
newList = []
for i in range(lstlen-1,-1,-1):
    newList.append(List[i])

print(newList)