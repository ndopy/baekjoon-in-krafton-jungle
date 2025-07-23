import sys

N, M = list(map(int, sys.stdin.readline().split()))
trees = list(map(int, sys.stdin.readline().split()))

def cut_tree(current_cut_height):
    result = 0

    for tree in trees:
        if tree > current_cut_height:
            result += (tree - current_cut_height)

    return result


def solution(tree_heights, target_tree_height):
    answer = 0
    start = 0
    end = max(tree_heights)

    while start <= end:
        mid = (start + end) // 2                  # 현재 시도하는 절단기 높이
        remaining_tree_height = cut_tree(mid)

        if remaining_tree_height >= target_tree_height:
            # 구하려는 M보다 더 많이 남은 경우, 일단 정답이 될 수 있으니 저장하기
            answer = mid
            # 절단기 높이를 좀 더 높이기 위해 탐색 범위를 수정하기
            start = mid + 1
        else:
            # 구하려는 M미터보다 더 적은 경우
            # 절단기 높이를 좀 더 낮추기 위해 탐색 범위를 수정하기
            end = mid - 1

    return answer

print(solution(trees, M))