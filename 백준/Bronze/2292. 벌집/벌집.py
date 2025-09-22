import sys

N = int(sys.stdin.readline())

if N == 1:
    print(1)
else:
    distance = 1
    max_value_at_distance = 1

    while N > max_value_at_distance:
        max_value_at_distance = max_value_at_distance + (6 * distance)
        distance += 1

    print(distance)