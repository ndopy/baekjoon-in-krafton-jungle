import sys

cards_count = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))

numbers_count = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

cards.sort()

# 이분 탐색
def binary_search(target, start, end):
    mid = (start + end) // 2
    if start > end:
        return 0
    if target == cards[mid]:
        return 1
    elif target < cards[mid]:
        return binary_search(target, start, mid - 1)
    else:
        return binary_search(target, mid + 1, end)

for number in numbers:
    print(binary_search(number, 0, cards_count - 1), end=' ')