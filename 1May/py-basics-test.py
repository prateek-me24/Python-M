##  1.


nums = [10,1,1,7,5,6,3,5,8,9,6,4,3]

print("original list : ", nums)
nums = set(nums)

nums = list(nums)

print("List after removing duplicates : ", nums)

print("Number of Unique Elements : ", len(nums))




##  2.


from itertools import permutations

elements = ('a', 'b', 'c')
perms = permutations(elements)
    
perms_list = list(perms)

for perm in perms_list:
    print(perm)





##  3.



from itertools import product

set1 = {1, 2, 3}
set2 = {'a', 'b', 'c'}

cartesian_prod = product(set1, set2)

cartesian_list = list(cartesian_prod)

for pair in cartesian_list:
    print(pair)





##  4.



tuple_of_integers = (5, 3, 8, 2, 9, 1)

maximum = max(tuple_of_integers)
minimum = min(tuple_of_integers)

print("Maximum element:", maximum)
print("Minimum element:", minimum)


##  custom code 

tuple_of_integers = (5, 3, 8, 2, 9, 1)
minimum = tuple_of_integers[0]
maximum = tuple_of_integers[1]

for i in range(len(tuple_of_integers)):
    if(tuple_of_integers[i] < minimum ):
        minimum = tuple_of_integers[i]
    if(tuple_of_integers[i]>maximum):
        maximum = tuple_of_integers[i]

print("maximum element : ",maximum)
print("minimum element : ", minimum)






##  5.


myList = [5,1,8,6,9,4,6]

myList.sort()
n = len(myList)

if(n%2!=0):
    median = myList[n//2]
else:
    firstval = myList[n//2-1]
    secondval = myList[n//2]
    median = (firstval+secondval)/2

print("Median : ", median)





##   6.


import operator

tuple1 = (1,4,7)
tuple2 = (2,5,8)

result = tuple(map(operator.add, tuple1, tuple2))
print(result)