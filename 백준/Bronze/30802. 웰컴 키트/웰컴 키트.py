import sys

N = int(sys.stdin.readline())
T_list = list(map(int, sys.stdin.readline().split()))
T, P = map(int, sys.stdin.readline().split())

# 티셔츠
bundle_of_t_shirt = 0

for i in range(len(T_list)):
    current_size_count = T_list[i]
    if current_size_count % T == 0:
        bundle_of_t_shirt += current_size_count // T
    else:
        bundle_of_t_shirt += (current_size_count // T) + 1

# 펜 묶음
bundle_of_pen = N // P
rest_of_pen = N % P

print(bundle_of_t_shirt)
print(bundle_of_pen, rest_of_pen)
