import sys

L = int(sys.stdin.readline())
chars = sys.stdin.readline()

def alphabet_to_num(char):
    # 'a'는 1이어야하므로 +1 처리를 해준다.
    return ord(char) - ord('a') + 1

H = 0

for i in range(L):
    num = alphabet_to_num(chars[i])
    H += num * pow(31, i)

print(H % 1234567891)