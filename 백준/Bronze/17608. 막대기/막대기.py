import sys

count_of_sticks = int(input())

sticks = list(map(int, sys.stdin.read().split()))
current_height = 0
answer = []

for _ in range(count_of_sticks):
    # 마지막 막대기부터 꺼내서 비교하기
    last_stick = sticks[-1]
    sticks.pop()

    if last_stick > current_height:
        answer.append(last_stick)
        current_height = last_stick

print(len(answer))

