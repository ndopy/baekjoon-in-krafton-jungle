import sys

count_of_numbers = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

def is_prime_number(number):
    if number == 1:
        return False

    if number == 2:
        return True

    for i in range(2, number):
        if (number % i) == 0: return False

    return True

prime_number_count = 0

for num in numbers:
    if is_prime_number(num): prime_number_count += 1

print(prime_number_count)