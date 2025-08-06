import sys

while True:
    test_case = sys.stdin.readline().strip()

    if not test_case:
        break

    if test_case == '0 0 0':
        break

    nums = list(map(int, test_case.split()))

    nums.sort()

    a, b, c = nums

    if a**2 + b**2 == c**2:
        print('right')
    else:
        print('wrong')