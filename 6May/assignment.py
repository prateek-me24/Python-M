#################     prime number function


def is_prime(val):
    if val <=1:
        return "wromg value"
    else:
        for i in range(2,val):
            if val%i==0:
                return "not a prime number"
            else:
                return "prime number"

value = int(input("Enter a number here : "))
print(is_prime(value))




####################      Triangle


def print_pattern(n):
    for i in range(n):
        print(" " * i + "*" * (2 * (n - i) - 1))

print_pattern(4)
