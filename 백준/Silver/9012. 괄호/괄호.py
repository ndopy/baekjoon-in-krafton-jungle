import sys

test_case_count = int(input().strip())

for _ in range(test_case_count):
    ps = sys.stdin.readline().strip()
    count = 0

    for char in ps:
        if char == '(':
            count += 1
        else:
            count -= 1

        if count < 0:
            break

    if count == 0:
        print('YES')
    else:
        print('NO')
