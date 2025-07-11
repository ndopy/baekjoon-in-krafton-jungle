# 4344
import sys
test_case_count = int(input())

for _ in range(test_case_count):
    numbers = list(map(int, sys.stdin.readline().split()))

    count_of_students = numbers[0]

    scores = numbers[1:]
    sum_of_scores = sum(scores)
    avg = sum_of_scores / count_of_students

    students_above_average = 0
    for score in scores:
        if score > avg:
            students_above_average += 1

    above_average_percentage = (students_above_average / count_of_students) * 100

    print(f"{above_average_percentage:.3f}%")