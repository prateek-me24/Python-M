###############  set

# collection of element, unique
# mutable in nature
# {}
# important set only have immutable datatype as element
# not have index positions

# myset = set({})
# print(type(myset))

myset = {10,20,30,30,30,30,30,30,"yash",(20,30)}
# print(myset)


myset.add(800)
# print(myset)

myset.update("uts")
# print(myset)

myset.remove(20)
# print(myset)

x = myset.pop()  ##  koi bhi random element delete kr dega

# print(x)
# print(myset)


myset.discard(10)  ## element ko remove krta h age element nhi milta to error nhi deta h



myset1 ={10,20,30}
myset2 = {30,40,50}

# print(myset1.union(myset2))

# print(myset1)



# print(myset)



###############    question      ###################
# "hey this side prateek hey"
# using set {hey thi prateek side}

# str_val = "hey this side prateek hey"

# data = str_val.split()

# data_set = set(data)
# print(data_set)


#################    question-2   ###################

day = int(input("enter neumeric value : "))
n = 0
start_value = 0
total_val = 0
day_week = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
for i in range(day):

    if day_week[i%7] == 'sunday':
        n = start_value
        n+=1
        start_value = n
        total_val += n
    else:
        n+=1
        total_val += n

print(total_val)



# " []{}()   "    =>   brackets are correct
# [ {} () ]   =>brackets are correct
# [ { ( ] } ]  => brackets are incorrect