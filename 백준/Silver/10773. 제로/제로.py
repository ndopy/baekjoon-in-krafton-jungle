import sys

lst = [0] * 100_000

count = int(sys.stdin.readline())
ptr = 0

for idx in range(count):
    number = int(sys.stdin.readline())

    if number == 0:
        ptr -= 1
        lst[ptr] = 0
    else:
        lst[ptr] = number
        ptr += 1

print(sum(lst))
