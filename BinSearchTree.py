class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        # Если дерево пустое, возвращаем новый узел
        if root is None:
            return TreeNode(key)

        # Иначе рекурсивно спускаемся по дереву
        if key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        return root

    def min_value_node(self, node):
        # Находим узел с минимальным значением
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete(self, root, key):
        # Если дерево пустое
        if root is None:
            return root

        # Иначе рекурсивно поищем удаляемый узел
        if key < root.val:
            root.left = self.delete(root.left, key)
        elif key > root.val:
            root.right = self.delete(root.right, key)
        else:
            # Узел с одним потомком или без потомков
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Узел с двумя потомками: получаем inorder преемника (наименьший в правом поддереве)
            temp = self.min_value_node(root.right)
            # Маленький узел заменяем удаляемым
            root.val = temp.val
            # Удаляем инордер преемника
            root.right = self.delete(root.right, temp.val)

        return root

    def search(self, root, key):
        # Базовый случай: корень — null или ключ присутствует в корне
        if root is None or root.val == key:
            return root

        # Ключ больше корня: ищем в правом поддереве
        if root.val < key:
            return self.search(root.right, key)

        # В противном случае, ищем в левом поддереве
        return self.search(root.left, key)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.val, end=' ')
            self.inorder(root.right)

# Пример использования
if __name__ == "__main__":
    bst = BinarySearchTree()
    root = None

    # Вставка элементов
    keys = [20, 15, 25, 10, 5, 30, 20, 19]
    for key in keys:
        root = bst.insert(root, key)

    print("Элементы в порядке возрастания:")
    bst.inorder(root)
    print()

    # Поиск элемента
    key_to_search = 15
    found_node = bst.search(root, key_to_search)
    if found_node:
        print(f"Элемент {key_to_search} найден.")
    else:
        print(f"Элемент {key_to_search} не найден.")

    # Удаление элемента
    key_to_delete = 15
    root = bst.delete(root, key_to_delete)
    print(f"Элементы после удаления {key_to_delete}:")
    bst.inorder(root)
    print()
