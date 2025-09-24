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
    left_right_reversed = []

    for line in original:
        left_right_reversed.append("".join(reversed(line)))

    print(*left_right_reversed, sep='\n')

else:
    up_down_reversed = list(reversed(original))

    print(*up_down_reversed, sep='\n')