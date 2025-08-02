import sys

matrix_count = int(sys.stdin.readline())
matrix = []
for _ in range(matrix_count):
    r, c = map(int, sys.stdin.readline().split())
    matrix.append((r, c))

dp = [[0] * matrix_count for _ in range(matrix_count)]

for partition_size in range(1, matrix_count):
    for partition_start in range(matrix_count - partition_size):
        partition_end = partition_start + partition_size
        dp[partition_start][partition_end] = float('inf')

        for partition_index in range(partition_start, partition_end):
            partition_left = dp[partition_start][partition_index]
            partition_right = dp[partition_index + 1][partition_end]
            partition_multiplication_result = matrix[partition_start][0] * matrix[partition_index][1] * matrix[partition_end][1]

            cost = partition_left + partition_right + partition_multiplication_result

            dp[partition_start][partition_end] = min(dp[partition_start][partition_end], cost)

print(dp[0][matrix_count - 1])
