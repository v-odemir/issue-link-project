"""A least recently used cache built on a doubly linked list."""

from ds.linked_list import DoubleNode


class LRUCache:
    """A fixed capacity cache that evicts the least recently used key."""

    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("capacity must be positive")
        self.capacity = capacity
        self._entries = {}
        self._head = None
        self._tail = None
        self.hits = 0
        self.misses = 0

    def __len__(self):
        return len(self._entries)

    def __contains__(self, key):
        return key in self._entries

    def __repr__(self):
        return "LRUCache({}/{})".format(len(self._entries), self.capacity)

    def _unlink(self, node):
        if node.prev is None:
            self._head = node.next
        else:
            node.prev.next = node.next
        if node.next is None:
            self._tail = node.prev
        else:
            node.next.prev = node.prev
        node.prev = None
        node.next = None

    def _push_front(self, node):
        node.prev = None
        node.next = self._head
        if self._head is not None:
            self._head.prev = node
        self._head = node
        if self._tail is None:
            self._tail = node

    def get(self, key, default=None):
        node = self._entries.get(key)
        if node is None:
            self.misses += 1
            return default
        self.hits += 1
        self._unlink(node)
        self._push_front(node)
        return node.value[1]

    def put(self, key, value):
        node = self._entries.get(key)
        if node is not None:
            node.value = (key, value)
            self._unlink(node)
            self._push_front(node)
            return
        if len(self._entries) >= self.capacity:
            self.evict()
        node = DoubleNode((key, value))
        self._entries[key] = node
        self._push_front(node)

    def evict(self):
        if self._tail is None:
            return None
        node = self._tail
        self._unlink(node)
        key = node.value[0]
        del self._entries[key]
        return key

    def keys(self):
        result = []
        node = self._head
        while node is not None:
            result.append(node.value[0])
            node = node.next
        return result

    def clear(self):
        self._entries.clear()
        self._head = None
        self._tail = None

    def hit_rate(self):
        total = self.hits + self.misses
        return 0.0 if total == 0 else self.hits / total
