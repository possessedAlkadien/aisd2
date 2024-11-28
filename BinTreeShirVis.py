class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Обход в глубину (DFS)
def preorder_traversal(node):
    if node is None:
        return []
    # Корень -> Левое поддерево -> Правое поддерево
    return [node.value] + preorder_traversal(node.left) + preorder_traversal(node.right)

# Обход в ширину (BFS)
from collections import deque

def level_order_traversal(root):
    if root is None:
        return []

    result = []
    queue = deque([root])

    while queue:
        current = queue.popleft()
        result.append(current.value)

        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)

    return result

if __name__ == "__main__":
    # Создаем пример дерева
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    # Выводим результат обходов
    print("Preorder Traversal:", preorder_traversal(root))
    print("Level Order Traversal:", level_order_traversal(root))
