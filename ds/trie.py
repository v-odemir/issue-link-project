"""A prefix tree for string keys."""


class TrieNode:
    """A node in the prefix tree."""

    __slots__ = ("children", "is_word", "value")

    def __init__(self):
        self.children = {}
        self.is_word = False
        self.value = None

    def __repr__(self):
        return "TrieNode({} children)".format(len(self.children))


class Trie:
    """Maps string keys to values with prefix lookups."""

    def __init__(self, words=None):
        self.root = TrieNode()
        self._size = 0
        for word in words or []:
            self.insert(word)

    def __len__(self):
        return self._size

    def __contains__(self, word):
        node = self._walk(word)
        return node is not None and node.is_word

    def __iter__(self):
        return iter(self.words())

    def __repr__(self):
        return "Trie({} words)".format(self._size)

    def _walk(self, prefix):
        node = self.root
        for char in prefix:
            node = node.children.get(char)
            if node is None:
                return None
        return node

    def insert(self, word, value=None):
        node = self.root
        for char in word:
            node = node.children.setdefault(char, TrieNode())
        if not node.is_word:
            self._size += 1
        node.is_word = True
        node.value = value

    def get(self, word, default=None):
        node = self._walk(word)
        if node is None or not node.is_word:
            return default
        return node.value

    def starts_with(self, prefix):
        return self._walk(prefix) is not None

    def with_prefix(self, prefix):
        node = self._walk(prefix)
        if node is None:
            return []
        found = []
        stack = [(node, prefix)]
        while stack:
            current, text = stack.pop()
            if current.is_word:
                found.append(text)
            for char, child in current.children.items():
                stack.append((child, text + char))
        found.sort()
        return found

    def words(self):
        return self.with_prefix("")

    def longest_prefix(self, text):
        node = self.root
        longest = ""
        current = ""
        for char in text:
            node = node.children.get(char)
            if node is None:
                break
            current += char
            if node.is_word:
                longest = current
        return longest

    def delete(self, word):
        path = [self.root]
        node = self.root
        for char in word:
            node = node.children.get(char)
            if node is None:
                return False
            path.append(node)
        if not node.is_word:
            return False
        node.is_word = False
        node.value = None
        self._size -= 1
        for index in range(len(path) - 1, 0, -1):
            child = path[index]
            if child.is_word or child.children:
                break
            del path[index - 1].children[word[index - 1]]
        return True
