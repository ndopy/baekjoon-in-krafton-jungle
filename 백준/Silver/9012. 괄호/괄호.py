import sys

test_case_count = int(input().strip())

for _ in range(test_case_count):
    ps = sys.stdin.readline().strip()
    ptr = 0

    ps_list = []

    for idx in range(len(ps)):
        bracket = ps[idx]

        # 첫 번째 항목은 바로 담기
        if len(ps_list) == 0:
            ps_list.append(bracket)
            ptr += 1
            continue

        # 두 번째 항목부터 짝이 맞는지 비교하기
        # 비교하는 괄호보다 먼저 들어간 괄호
        prev = ps_list[ptr -1]

        if prev + bracket == "()": # 짝이 맞으면
            # 현재 괄호를 넣지 않고 prev 를 제거하기
            ptr -= 1
            ps_list.pop()

        else: # 짝이 안 맞으면
            ps_list.append(bracket)
            ptr += 1

    # 모든 괄호에 대해 실행했는데, 리스트가 비어 있지 않다면
    # 짝이 맞는 괄호를 찾는 데에 실패한 케이스가 있다는 것이다.
    if len(ps_list):
        print('NO')
    else:
        print('YES')
