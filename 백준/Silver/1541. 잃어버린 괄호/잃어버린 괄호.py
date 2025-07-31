import sys

expression = sys.stdin.readline().strip()


def add_brackets(exp):
    # '-' 문자를 기준으로 식을 나누기
    # ex: "50+40-30+20" -> ['50+40', '30+20']
    parts = exp.split('-')

    # 첫 번째 부분의 합을 계산 -> 이 값은 항상 양수.
    # '50+40' -> 90
    result = sum(map(int, parts[0].split('+')))

    # 나머지 부분들을 순회하며 각 부분의 합을 결과에서 빼기
    # '30+20' -> 50
    # result = 90 - 50
    for part in parts[1:]:
        result -= sum(map(int, part.split('+')))

    print(result)

add_brackets(expression)



