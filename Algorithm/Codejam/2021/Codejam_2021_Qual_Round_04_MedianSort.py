'''
2021 Codejam Qualification Round
04_Median Sort

※ increasing, decreasing order 상관 여부
※ 완전 탐색 가능 여부 (N 고려)
'''

# 이 방법은 안 될 듯
# 이진 탐색 트리는 크기 비교가 가능해야하는데
# 중위값만으로 위치를 찾을 수 있을 거라고 생각했는데
# 마지막에 print할 때 왼쪽부터 출력을 할 때
# 순서대로 정렬되어있지 않을 것 같다
class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class BinarySearchTree(object):
    def __init__(self):
        self.root = None

class BinarySearchTree(object):
    ...
    def insert(self, data):
        self.root = self._insert_value(self.root, data)
        return self.root is not None

    def _insert_value(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if data <= node.data:
                node.left = self._insert_value(node.left, data)
            else:
                node.right = self._insert_value(node.right, data)
        return node
    
T, N, Q = map(int, input().split())
for t in range(T):
    new_tree = BinarySearchTree()
    # 처음에 세 개 물어보기
    print("1 2 3")
    # 나온 답으로 이진 트리 구성
    mid = int(input())
    for i in [1, 2, 3]:
        if mid == i:

    # 이진트리에 이미 있는 부모 2개 + 아직 물어보지 않은 것 포함해서
    # 출력할 수 있도록...
    
