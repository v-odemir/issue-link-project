"""A binary min-heap and a priority queue built on top of it."""


class MinHeap:
    """A binary min-heap over comparable items."""

    def __init__(self, items=None):
        self._items = list(items or [])
        if self._items:
            self._heapify()

    def __len__(self):
        return len(self._items)

    def __bool__(self):
        return bool(self._items)

    def __repr__(self):
        return "MinHeap({})".format(self._items)

    def _heapify(self):
        for index in reversed(range(len(self._items) // 2)):
            self._sift_down(index)

    def _sift_up(self, index):
        item = self._items[index]
        while index > 0:
            parent = (index - 1) // 2
            if self._items[parent] <= item:
                break
            self._items[index] = self._items[parent]
            index = parent
        self._items[index] = item

    def _sift_down(self, index):
        size = len(self._items)
        item = self._items[index]
        while True:
            left = 2 * index + 1
            if left >= size:
                break
            smallest = left
            right = left + 1
            if right < size and self._items[right] < self._items[left]:
                smallest = right
            if self._items[smallest] >= item:
                break
            self._items[index] = self._items[smallest]
            index = smallest
        self._items[index] = item

    def push(self, item):
        self._items.append(item)
        self._sift_up(len(self._items) - 1)

    def pop(self):
        if not self._items:
            raise IndexError("pop from empty heap")
        smallest = self._items[0]
        last = self._items.pop()
        if self._items:
            self._items[0] = last
            self._sift_down(0)
        return smallest

    def peek(self):
        if not self._items:
            raise IndexError("peek at empty heap")
        return self._items[0]

    def push_pop(self, item):
        if self._items and self._items[0] < item:
            item, self._items[0] = self._items[0], item
            self._sift_down(0)
        return item

    def to_sorted_list(self):
        clone = MinHeap(self._items)
        return [clone.pop() for _ in range(len(clone))]


class PriorityQueue:
    """A stable priority queue: equal priorities keep insertion order."""

    def __init__(self):
        self._heap = MinHeap()
        self._counter = 0

    def __len__(self):
        return len(self._heap)

    def __bool__(self):
        return bool(self._heap)

    def __repr__(self):
        return "PriorityQueue({} items)".format(len(self._heap))

    def push(self, item, priority):
        self._heap.push((priority, self._counter, item))
        self._counter += 1

    def pop(self):
        if not self._heap:
            raise IndexError("pop from empty queue")
        _, _, item = self._heap.pop()
        return item

    def peek(self):
        if not self._heap:
            raise IndexError("peek at empty queue")
        return self._heap.peek()[2]

    def drain(self):
        return [self.pop() for _ in range(len(self._heap))]


def heap_sort(items):
    """Sort a list in ascending order using a min-heap."""
    return MinHeap(items).to_sorted_list()


def n_smallest(items, count):
    """Return the count smallest items in ascending order."""
    if count <= 0:
        return []
    heap = MinHeap(items)
    limit = min(count, len(heap))
    return [heap.pop() for _ in range(limit)]
