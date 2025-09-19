import sys

# 3개의 문자열 다음에 올 숫자(i)를 어떻게 찾을 것인가?

# a, b, c 중에 숫자를 찾아야, 다음에 올 숫자(=문자열)을 찾을 수 있다.
# a가 숫자라면? -> i = a + 3
# b가 숫자라면? -> i = b + 2
# c가 숫자라면? -> i = c + 1
# a, b, c 가 모두 숫자가 아니라면? -> 이 경우가 없다는 걸 어떻게 증명하지?

a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()
c = sys.stdin.readline().strip()

i = 0

if a.isdigit():
    i = int(a) + 3
elif b.isdigit():
    i = int(b) + 2
elif c.isdigit():
    i = int(c) + 1

if i % 3 == 0 and i % 5 == 0:
    print('FizzBuzz')
elif i % 3 == 0 and i % 5 != 0:
    print('Fizz')
elif i % 3 != 0 and i % 5 == 0:
    print('Buzz')
elif i % 3 != 0 and i % 5 != 0:
    print(i)