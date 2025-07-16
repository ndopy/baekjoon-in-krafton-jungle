import sys

def get_permutations(current_combination, remaining_items, target_count, results):
    if len(current_combination) == target_count:
        results.append(list(current_combination))
        return

    for i in range(len(remaining_items)):
        current_item = remaining_items[i]
        current_combination.append(current_item)
        current_remaining_items = remaining_items[:i] + remaining_items[i+1:]

        get_permutations(
            current_combination,
            current_remaining_items,
            target_count,
            results
        )
        
        current_combination.pop()


target_count = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

all_permutations = []
get_permutations([], numbers, target_count, all_permutations)

max_total_diff = 0

for perm in all_permutations:
    current_diff_sum = 0

    for i in range(len(perm) - 1):
        current_diff_sum += abs(perm[i] - perm[i+1])
        
    if current_diff_sum > max_total_diff:
        max_total_diff = current_diff_sum

print(max_total_diff)