import sys

# 파이썬 재귀 호출 깊이 제한을 10^5 (10만)으로 늘림
sys.setrecursionlimit(10**5)

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(current_node, new_value):
    if current_node is None:
        return Node(new_value)

    if new_value < current_node.value:
        current_node.left = insert(current_node.left, new_value)
    elif new_value > current_node.value:
        current_node.right = insert(current_node.right, new_value)

    return current_node

def post_order_traversal(node):
    if node:
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        print(node.value)

root = None
input_data = []

while True:
    line = sys.stdin.readline()

    if not line:
        break
    input_data.append(int(line))

if input_data:
    root = Node(input_data[0])

    for i in range(1, len(input_data)):
        insert(root, input_data[i])

post_order_traversal(root)
