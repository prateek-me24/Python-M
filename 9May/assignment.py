################    4


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


n = 10
if n <= 0:
    print("Please enter a positive integer.")
else:
    print("Fibonacci Series:")
    for i in range(n):
        print(fibonacci(i), end=" ")





print()
################       5

input_string = "Hello, World!"
check_dict = {}

for i in input_string:
    if i not in check_dict: 
        check_dict[i] = 1
    else:
        check_dict[i] = check_dict[i]+1

print(check_dict)




print()
############        6 


def capitalize_words_in_tuple(tuple_of_strings):
    capitalized_words = tuple(word.capitalize() for word in tuple_of_strings)
    return capitalized_words


input_tuple = ("hello", "world", "python", "programming")
output_tuple = capitalize_words_in_tuple(input_tuple)
print("Original Tuple : ", input_tuple)
print("Tuple with Capitalized Words : ", output_tuple)




print()
############        7

def find_max_of_three(a, b, c):
    max_num = a
    if b > max_num:
        max_num = b
    if c > max_num:
        max_num = c
    return max_num

num1 = 10
num2 = 25
num3 = 15
maximum = find_max_of_three(num1, num2, num3)
print("Maximum of the three numbers:", maximum)



print()
###########        8

rows=5

for i in range(1, rows + 1):
    if i % 2 != 0:  
        for j in range(65, 65 + i):
            print(chr(j), end=" ")
    else: 
        for j in range(1, i + 1):
            print(j, end=" ")
    print()




print()
############        9

start_num = 1
start_char = 65 
rows = 10

for i in range(0, rows):
    if i%2==0:
        for j in range(i+2):
            if j % 2 == 0:  
                print(start_num ** 2, end=" ")
                start_num += 1
            else:  
                print(chr(start_char), end=" ")
                start_char += 1
        print()
    else:
        pass


print()
##########        10


rows = 5

for i in range(rows, 0, -1):  # Loop for the upper half
    print("  " * (rows - i), end="")  # Print leading spaces
    print("* " * i)

for i in range(2, rows + 1):  # Loop for the lower half
    print("  " * (rows - i), end="")  # Print leading spaces
    print("* " * i)
