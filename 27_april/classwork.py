########## dictonary

# collection of element
# comma saperated
# kay:value (element)
# key:value, key:value
# don't  have index position
# mutable in nature


myDict = {1:'prateek', 2:'tushar', 3:'aman', 'company':'regex'}

# print(myDict)


# print(myDict[1])

# # update value
# myDict[2] = 'yash'
# print(myDict)

# #insert
# myDict[4] = 500
# print(myDict)


# # delete and return

# x=myDict.pop(2)
# print(myDict, x)


# # key value pair delete and return

# z = myDict.popitem()
# print(z)


# print(myDict)


# print( 1 in myDict)

# print(myDict.keys())
# print(myDict.values())
# print(myDict.items())


x=200

if(x not in myDict):
    myDict[x] = 1

print(myDict)



str_val = "hello prateek"

##   first method
len_str = 0
for i in str_val:
    len_str+=1

check_key = "totalcharacters"
myDict[check_key] = len_str
print(myDict)

## second methos

mynewDict = {}
for i in str_val:
    if 'total' not in mynewDict:
        mynewDict['total'] = 1
    else:
        mynewDict['total'] = mynewDict['total']+1

print(mynewDict)





str_val = "hello prateek hello hey"

check_dict = {}

for i in str_val:
    if i not in check_dict: 
        check_dict[i] = 1
    else:
        check_dict[i] = check_dict[i]+1

print(check_dict)





str_val = "hello prateek hello hey"
vowels = "aeiouAEIOU"
vowelCount = 0
for i in str_val:
    if i in vowels:
        vowelCount+=1
print(vowelCount)