import sys

test_case_count = int(sys.stdin.readline())

for _ in range(test_case_count):
    flower = sys.stdin.readline().strip()

    mid = len(flower) // 2

    if flower[mid - 1] == flower[mid]:
        print('Do-it')
    else:
        print('Do-it-Not')