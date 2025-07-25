import sys

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preorder(node):
    if node:
        print(node.value, end='')
        preorder(node.left)
        preorder(node.right)

def inorder(node):
    if node:
        inorder(node.left)
        print(node.value, end='')
        inorder(node.right)

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.value, end='')

node_count = int(sys.stdin.readline())

input_data = []
node_dict = {}

for _ in range(node_count):
    current_input = list(sys.stdin.readline().split())
    input_data.append(current_input)

    # 현재 value에 대한 노드를 생성하기
    value = current_input[0]
    node = Node(value)

    # 생성한 노드를 노드 저장소에 넣기
    node_dict[value] = node

for node_data in input_data:
    value, left, right = node_data
    # value 에 해당하는 노드에 left 와 right 를 연결하기
    if left != '.':
        node_dict[value].left = node_dict[left]

    if right != '.':
        node_dict[value].right = node_dict[right]

root = node_dict['A']

preorder(root)
print()
inorder(root)
print()
postorder(root)

