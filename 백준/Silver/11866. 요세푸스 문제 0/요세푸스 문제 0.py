import sys
from collections import deque

N, K = list(map(int, sys.stdin.readline().split()))

def josephus_with_deque(n, k):
    people_queue = deque(range(1, n + 1))
    result = []

    while people_queue:
        # 앞에서부터 (k - 1)명을 뒤로 보내기
        for _ in range(k - 1):
            person = people_queue.popleft()
            people_queue.append(person)

        removed_person = people_queue.popleft()
        result.append(removed_person)

    return result

answer = josephus_with_deque(N, K)
print(f'<{", ".join(map(str, answer))}>')