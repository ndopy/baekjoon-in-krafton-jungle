import sys

N = int(sys.stdin.readline())

problems = {}
min_level = 4

for _ in range(N):
    problem, level = sys.stdin.readline().split()
    level = int(level)

    problems[level] = problem

    if level < min_level:
        min_level = level

print(problems[min_level])