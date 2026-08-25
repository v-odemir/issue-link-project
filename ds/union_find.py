"""Disjoint set union with path compression and union by size."""


class UnionFind:
    """Tracks disjoint sets over hashable elements."""

    def __init__(self, elements=None):
        self._parent = {}
        self._size = {}
        self._groups = 0
        for element in elements or []:
            self.add(element)

    def __len__(self):
        return len(self._parent)

    def __contains__(self, element):
        return element in self._parent

    def __repr__(self):
        return "UnionFind({} elements, {} groups)".format(len(self._parent), self._groups)

    @property
    def groups(self):
        return self._groups

    def add(self, element):
        if element in self._parent:
            return False
        self._parent[element] = element
        self._size[element] = 1
        self._groups += 1
        return True

    def find(self, element):
        if element not in self._parent:
            raise KeyError(element)
        root = element
        while self._parent[root] != root:
            root = self._parent[root]
        while self._parent[element] != root:
            self._parent[element], element = root, self._parent[element]
        return root

    def union(self, left, right):
        self.add(left)
        self.add(right)
        left_root = self.find(left)
        right_root = self.find(right)
        if left_root == right_root:
            return False
        if self._size[left_root] < self._size[right_root]:
            left_root, right_root = right_root, left_root
        self._parent[right_root] = left_root
        self._size[left_root] += self._size[right_root]
        self._groups -= 1
        return True

    def connected(self, left, right):
        return self.find(left) == self.find(right)

    def group_size(self, element):
        return self._size[self.find(element)]

    def to_groups(self):
        buckets = {}
        for element in self._parent:
            buckets.setdefault(self.find(element), []).append(element)
        return list(buckets.values())
