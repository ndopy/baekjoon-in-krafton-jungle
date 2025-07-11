import sys

data = sys.stdin.readline().split()

num_str1 = reversed(data[0])
num_str2 = reversed(data[1])
sangsu_num1 = int(''.join(num_str1))
sangsu_num2 = int(''.join(num_str2))

print(max(sangsu_num1, sangsu_num2))
