import sys
from collections import deque

test_case_count = int(sys.stdin.readline())

for _ in range(test_case_count):
    # 문서의 개수, Queue 안에서의 문서의 위치
    documents_count, target_position = map(int, sys.stdin.readline().split())

    # 중요도
    weight = list(map(int, sys.stdin.readline().split()))

    # deque 사용하기
    documents = deque()

    # 몇 번 인쇄했는지 세는 카운트
    print_count = 0

    # [중요도, 문서 번호] 형태로 집에 넣기
    for i in range(documents_count):
        documents.append([weight[i], i])

    # 중요도를 오름차순으로 정렬하고, 중복값을 제거하기
    weight.sort()

    # 나머지 문서들을 확인하면서 current_weight 보다 높은 문서가 하나라도 있으면 이 문서를 큐의 가장 뒤에 재배치하기
    while documents:
        # 큐에서 가장 앞에 있는 문서의 '중요도'를 확인하기
        current_weight, current_position = documents[0]

        # 현재 가장 높은 가중치
        current_max_weight = weight[-1]

        # 현재 문서의 중요도가 가장 높지 않다면 큐의 제일 마지막으로 삽입하기
        if current_weight < current_max_weight:
            documents.popleft()
            documents.append([current_weight, current_position])
        else:
            # 현재 문서의 중요도가 가장 높다면 인쇄하기
            documents.popleft()
            print_count += 1
            # 현재 중요도를 중요도 목록에서 pop
            weight.pop()

            if current_position == target_position:
                break

    print(print_count)


