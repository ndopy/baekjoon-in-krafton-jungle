import sys

T = int(sys.stdin.readline())

for _ in range(T):
    value_str, unit = sys.stdin.readline().split()
    value = float(value_str)
    # print(f"{value} {unit}")

    if unit == 'kg':
        print(f"{value * 2.2046:.4f} lb")
    elif unit == 'lb':
        print(f"{value * 0.4536:.4f} kg")
    elif unit == 'l':
        print(f"{value * 0.2642:.4f} g")
    elif unit == 'g':
        print(f"{value * 3.7854:.4f} l")