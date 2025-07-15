import sys

counting_list = [0] * (10_000 + 1)

count = int(sys.stdin.readline())

for _ in range(count):
    number = int(sys.stdin.readline())
    counting_list[number] += 1

for idx in range(len(counting_list)):
    count_of_number = counting_list[idx]

    if count_of_number > 0:
        for _ in range(count_of_number):
            print(idx)
