import sys

N = int(sys.stdin.readline())

members = []

# i = 가입한 순서
for i in range(N):
    age_str, name = sys.stdin.readline().strip().split()
    age = int(age_str)

    members.append((i, age, name))

# age, i 순서대로 정렬하기
members.sort(key=lambda x: (x[1], x[0]))

for i in range(N):
    print(f"{members[i][1]} {members[i][2]}")