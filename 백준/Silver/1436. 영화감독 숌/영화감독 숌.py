import sys

N = int(sys.stdin.readline())

number = 0
count = 0

while count < N:
    number += 1

    if '666' in str(number):
        count += 1


print(number)