# N - 원판 개수
# start - 시작 기둥 (왼쪽)
# temp - 임시 기둥 (가운데)
# destination - 목표 기둥 (오른쪽)

N = int(input())

def hanoi(N, start, destination, temp):

    # 원판이 1개라면
    if N == 1:
        print(f'{start} {destination}')
        return

    # 원판이 2개 이상
    # 1) N-1 만큼의 원판을 시작 기둥에서 임시 기둥으로 옮긴다. (= 임시 기둥이 곧 목표 기둥이 된다.)
    hanoi(N-1, start, temp, destination)

    print(f'{start} {destination}')

    # 2) 임시 기둥에 있는 원판을 목표 기둥으로 옮긴다. (= 임시 기둥이 곧 시작 기둥이 된다.)
    hanoi(N-1, temp, destination, start)


# 옮긴 횟수 : 2^N - 1
print(2 ** N - 1)

if N <= 20:
    hanoi(N, 1, 3, 2)