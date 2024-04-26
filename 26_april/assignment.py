##  1.
################   Armstrong number 4 digits


num = 9474
check = num
x = 0
dig = len(str(num))

while True:
    x += (num%10)**dig
    num = num//10

    if num == 0:
        break

if(x==check):
    print(check, ' is a armstrong number')
else:
    print(check, ' not armstrong value')




##  2.
###############  to find all the unique word from a string no duplicancy

data = "hey hello user prateek prateek hello"

myList = data.split()
uniqueList = []

for i in myList:
    if myList.count(i)==1:
        uniqueList.append(i)

print(uniqueList)
