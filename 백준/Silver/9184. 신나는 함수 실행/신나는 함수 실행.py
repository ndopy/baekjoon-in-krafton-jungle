import sys

input_data = []
memo = {}

def w(a, b, c):
    if (a, b, c) in memo:
        return memo[(a, b, c)]

    if a<=0 or b<=0 or c<=0:
        result = 1
    elif a>20 or b>20 or c>20:
        result = w(20, 20, 20)
    elif a<b and b<c:
        result = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        memo[(a, b, c)] = result
    else:
        result = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        memo[(a, b, c)] = result

    return result


while True:
    line = sys.stdin.readline().rstrip()

    if line == '-1 -1 -1':
        break
    input_data.append(tuple(map(int, line.split())))

if input_data:

    for data in input_data:
        a, b, c = data
        print(f"w({a}, {b}, {c}) = {w(a, b, c)}")