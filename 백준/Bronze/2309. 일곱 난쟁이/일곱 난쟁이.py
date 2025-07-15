import sys

# 아홉 난쟁이들의 키를 담은 리스트
heights_of_nine_dwarfs = list(map(int, sys.stdin.read().split()))
N = len(heights_of_nine_dwarfs)

# 아홉 난쟁이들의 키의 합
sum_of_nine_dwarfs_heights = sum(heights_of_nine_dwarfs)

# 제외될 난쟁이 2명의 키의 합
height_difference = sum_of_nine_dwarfs_heights - 100

# 제외할 난쟁이들의 키
height_of_first_dwarf = 0
height_of_second_dwarf = 0

for i in range(N):
    for j in range(i+1, N):

        if heights_of_nine_dwarfs[i] + heights_of_nine_dwarfs[j] == height_difference:
            # i번째, j번째 난쟁이가 제외되어야 한다.
            height_of_first_dwarf = heights_of_nine_dwarfs[i]
            height_of_second_dwarf = heights_of_nine_dwarfs[j]
            break

    if height_of_first_dwarf != 0:  # 제외할 난쟁이를 찾았으면 루프를 멈춰야 한다.
        break

# 진짜 난쟁이들의 키만 담을 리스트
real_dwarfs_heights = []

for height in heights_of_nine_dwarfs:
    if height == height_of_first_dwarf:
        height_of_first_dwarf = -1
    elif height == height_of_second_dwarf:
        height_of_second_dwarf = -1
    else:
        real_dwarfs_heights.append(height)

real_dwarfs_heights.sort()

for height in real_dwarfs_heights:
    print(height)
