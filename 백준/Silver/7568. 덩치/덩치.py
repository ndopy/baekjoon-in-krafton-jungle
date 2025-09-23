import sys

persons = []

N = int(sys.stdin.readline())

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    persons.append((x, y))

answer = []

for person1 in persons:
    person1_weight = person1[0]
    person1_height = person1[1]
    count = 1

    for person2 in persons:
        if person1 == person2:
            continue

        person2_weight = person2[0]
        person2_height = person2[1]

        if person1_weight < person2_weight and person1_height < person2_height:
            count += 1

    answer.append(count)

print(*answer, sep=' ')