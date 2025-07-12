def get_max_area():
    w, h = map(int, input().split())
    n = int(input())

    horizontal_cuts = [0, h]
    vertical_cuts = [0, w]

    for _ in range(n):
        direction, cut_point = map(int, input().split())
        if direction == 0:
            horizontal_cuts.append(cut_point)
        else:
            vertical_cuts.append(cut_point)

    horizontal_cuts.sort()
    vertical_cuts.sort()

    max_h = 0
    for i in range(1, len(horizontal_cuts)):
        max_h = max(max_h, horizontal_cuts[i] - horizontal_cuts[i - 1])

    max_v = 0
    for i in range(1, len(vertical_cuts)):
        max_v = max(max_v, vertical_cuts[i] - vertical_cuts[i - 1])

    print(max_h * max_v)


get_max_area()