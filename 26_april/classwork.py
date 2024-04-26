# data = "hey prateek hey"

# x = data.split(" ")

# print(x, type(x))



# data = "hey prateek hey hello hey user user hey"

# li = data.split(" ")
# newLi = []
# for i in li:
#     if(i not in newLi):
#         newLi.append(i)

# print(newLi)




#################       tuple

# collection of multiple element
# immutable
# index positions
# we declared this in parentheses ()
# tuple m parentheses compulsary nhi hote h , saperated values ko like a tuple hi read krte h 

# mytuple = 10
# print(type(mytuple))

# mytuple = 10,   # tuple m single value store krwani ho to value k baad , lgana hota h
# print(type(mytuple))

# mytuple = 10,20
# print(type(mytuple))


# mytuple = (10,20,'hello', 10.2)
# print(mytuple[0:3])

# print(mytuple.index('hello'))

# print(id(mytuple))

# mytuple = mytuple+(60,70,80)
# print(id(mytuple))



##########   Please check

# value = "hey prateek hey hello hello prateek prateek"

# myList = value.split()
# tuple(myList)
# print('hey in ',myList.count('hey'), ' time in value')
# print('hello in ',myList.count('hello'), ' time in value')
# print('prateek in ',myList.count('prateek'), ' time in value')



################   Armstrong number 3 digits


num = 154
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