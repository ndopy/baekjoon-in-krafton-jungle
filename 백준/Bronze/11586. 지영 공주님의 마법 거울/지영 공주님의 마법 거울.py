import sys

N = int(sys.stdin.readline())

original = []

for _ in range(N):
    line = sys.stdin.readline().strip()
    original.append(line)

emotion = int(sys.stdin.readline())

if emotion == 1:
    print(*original, sep='\n')
elif emotion == 2:
    left_right_reversed = [line[::-1] for line in original]
    print(*left_right_reversed, sep='\n')
else:
    up_down_reversed = original[::-1]
    print(*up_down_reversed, sep='\n')