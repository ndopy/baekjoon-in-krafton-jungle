import sys

test_case_count = int(sys.stdin.readline())

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5)+ 1):
        if n % i == 0:
            return False
    return True

def get_goldbach_partitions(n):
    for i in range(n//2, 1, -1):
        if is_prime(i) and is_prime(n - i):
            print(i, n-i)
            return None
    return None

for i in range(test_case_count):
    number = int(sys.stdin.readline())
    get_goldbach_partitions(number)