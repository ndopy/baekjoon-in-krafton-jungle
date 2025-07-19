import sys

arr_size = int(sys.stdin.readline())
arr =  list(map(int, sys.stdin.readline().split()))

count = int(sys.stdin.readline())
numbers_to_find = list(map(int, sys.stdin.readline().split()))

def binary_search(target: int, sorted_list: list) -> int:
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2         # mid = 중간 인덱스

        if target == sorted_list[mid]:    # 타겟과 같은 값을 찾은 경우
            return 1
        elif target > sorted_list[mid]:   # 타겟이 중간값 보다 크면 -> 오른쪽 탐색
            left = mid + 1                # 검색 범위 재설정
        elif target < sorted_list[mid]:   # 타겟이 중간값보다 작은 경우
            right = mid - 1               # 검색 범위 재설정

    return 0

# 오름차순으로 정렬하기
arr.sort()

for number in numbers_to_find:
    print(binary_search(number, arr))