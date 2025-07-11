import sys

test_case_count = input()

for _ in range(int(test_case_count)):
    data = sys.stdin.readline().split()
    repeat_count = int(data[0])
    chars = list(data[1])

    answer = ''

    for char in chars:
        answer += char * repeat_count

    print(answer)