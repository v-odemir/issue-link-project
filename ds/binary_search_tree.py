"""An unbalanced binary search tree with the usual traversals."""


class TreeNode:
    """A binary search tree node."""

    __slots__ = ("key", "value", "left", "right")

    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return "TreeNode({!r})".format(self.key)


class BinarySearchTree:
    """Maps ordered keys to values; duplicate keys overwrite the value."""

    def __init__(self, pairs=None):
        self.root = None
        self._size = 0
        for key, value in pairs or []:
            self.insert(key, value)

    def __len__(self):
        return self._size

    def __contains__(self, key):
        return self._find(key) is not None

    def __iter__(self):
        return iter(self.keys())

    def __repr__(self):
        return "BinarySearchTree({} keys)".format(self._size)

    def insert(self, key, value=None):
        if self.root is None:
            self.root = TreeNode(key, value)
            self._size += 1
            return
        current = self.root
        while True:
            if key == current.key:
                current.value = value
                return
            if key < current.key:
                if current.left is None:
                    current.left = TreeNode(key, value)
                    self._size += 1
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = TreeNode(key, value)
                    self._size += 1
                    return
                current = current.right

    def get(self, key, default=None):
        node = self._find(key)
        return default if node is None else node.value

    def _find(self, key):
        current = self.root
        while current is not None:
            if key == current.key:
                return current
            current = current.left if key < current.key else current.right
        return None

    def minimum(self):
        if self.root is None:
            raise ValueError("empty tree")
        current = self.root
        while current.left is not None:
            current = current.left
        return current.key

    def maximum(self):
        if self.root is None:
            raise ValueError("empty tree")
        current = self.root
        while current.right is not None:
            current = current.right
        return current.key

    def delete(self, key):
        self.root, removed = self._delete(self.root, key)
        if removed:
            self._size -= 1
        return removed

    def _delete(self, node, key):
        if node is None:
            return None, False
        if key < node.key:
            node.left, removed = self._delete(node.left, key)
            return node, removed
        if key > node.key:
            node.right, removed = self._delete(node.right, key)
            return node, removed
        if node.left is None:
            return node.right, True
        if node.right is None:
            return node.left, True
        successor = node.right
        while successor.left is not None:
            successor = successor.left
        node.key = successor.key
        node.value = successor.value
        node.right, _ = self._delete(node.right, successor.key)
        return node, True

    def in_order(self):
        result = []
        stack = []
        current = self.root
        while stack or current is not None:
            while current is not None:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.key)
            current = current.right
        return result

    def pre_order(self):
        result = []
        stack = [self.root] if self.root is not None else []
        while stack:
            node = stack.pop()
            result.append(node.key)
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
        return result

    def post_order(self):
        result = []
        stack = [self.root] if self.root is not None else []
        while stack:
            node = stack.pop()
            result.append(node.key)
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)
        result.reverse()
        return result

    def level_order(self):
        if self.root is None:
            return []
        result = []
        queue = [self.root]
        index = 0
        while index < len(queue):
            node = queue[index]
            index += 1
            result.append(node.key)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        return result

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return 0
        return 1 + max(self._height(node.left), self._height(node.right))

    def is_balanced(self):
        return self._balance(self.root) is not None

    def _balance(self, node):
        if node is None:
            return 0
        left = self._balance(node.left)
        if left is None:
            return None
        right = self._balance(node.right)
        if right is None or abs(left - right) > 1:
            return None
        return 1 + max(left, right)

    def keys(self):
        return self.in_order()

    def values(self):
        return [self.get(key) for key in self.in_order()]
