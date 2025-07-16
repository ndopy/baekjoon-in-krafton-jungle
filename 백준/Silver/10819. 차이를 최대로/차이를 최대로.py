import sys

max_total_diff = 0

def get_permutations(current_combination, remaining_items, target_count, results):

    if len(current_combination) == target_count:
        current_diff_sum = 0

        for i in range(len(current_combination) - 1):
            current_diff_sum += abs(current_combination[i] - current_combination[i+1])

        global max_total_diff
        if current_diff_sum > max_total_diff:
            max_total_diff = current_diff_sum
            
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

get_permutations([], numbers, target_count, [])

print(max_total_diff)