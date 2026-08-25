"""Singly and doubly linked list implementations."""


class Node:
    """A single link in a singly linked list."""

    __slots__ = ("value", "next")

    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

    def __repr__(self):
        return "Node({!r})".format(self.value)


class LinkedList:
    """A singly linked list with O(1) push_front and push_back."""

    def __init__(self, items=None):
        self.head = None
        self.tail = None
        self._size = 0
        for item in items or []:
            self.push_back(item)

    def __len__(self):
        return self._size

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def __repr__(self):
        return "LinkedList({})".format(list(self))

    def push_front(self, value):
        node = Node(value, self.head)
        self.head = node
        if self.tail is None:
            self.tail = node
        self._size += 1
        return node

    def push_back(self, value):
        node = Node(value)
        if self.tail is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self._size += 1
        return node

    def pop_front(self):
        if self.head is None:
            raise IndexError("pop from empty list")
        node = self.head
        self.head = node.next
        if self.head is None:
            self.tail = None
        self._size -= 1
        return node.value

    def find(self, value):
        index = 0
        for item in self:
            if item == value:
                return index
            index += 1
        return -1

    def remove(self, value):
        previous = None
        current = self.head
        while current is not None:
            if current.value == value:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                if current is self.tail:
                    self.tail = previous
                self._size -= 1
                return True
            previous = current
            current = current.next
        return False

    def reverse(self):
        previous = None
        current = self.head
        self.tail = self.head
        while current is not None:
            following = current.next
            current.next = previous
            previous = current
            current = following
        self.head = previous
        return self

    def to_list(self):
        return list(self)


class DoubleNode:
    """A single link in a doubly linked list."""

    __slots__ = ("value", "prev", "next")

    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

    def __repr__(self):
        return "DoubleNode({!r})".format(self.value)


class Deque:
    """A double ended queue backed by a doubly linked list."""

    def __init__(self, items=None):
        self.head = None
        self.tail = None
        self._size = 0
        for item in items or []:
            self.append(item)

    def __len__(self):
        return self._size

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def __repr__(self):
        return "Deque({})".format(list(self))

    def append(self, value):
        node = DoubleNode(value)
        if self.tail is None:
            self.head = node
        else:
            node.prev = self.tail
            self.tail.next = node
        self.tail = node
        self._size += 1
        return node

    def append_left(self, value):
        node = DoubleNode(value)
        if self.head is None:
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
        self.head = node
        self._size += 1
        return node

    def pop(self):
        if self.tail is None:
            raise IndexError("pop from empty deque")
        node = self.tail
        self.tail = node.prev
        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None
        self._size -= 1
        return node.value

    def pop_left(self):
        if self.head is None:
            raise IndexError("pop from empty deque")
        node = self.head
        self.head = node.next
        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None
        self._size -= 1
        return node.value
