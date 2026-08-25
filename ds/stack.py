"""A stack with a balanced bracket checker built on top of it."""
__all__ = ["Stack", "is_balanced", "evaluate_postfix"]


class Stack:
    """A last-in first-out stack backed by a Python list."""

    PAIRS = {")": "(", "]": "[", "}": "{"}

    def __init__(self, items=None):
        self._items = list(items or [])

    def __len__(self):
        return len(self._items)

    def __bool__(self):
        return bool(self._items)

    def __iter__(self):
        return reversed(self._items)

    def __repr__(self):
        return "Stack({})".format(self._items)

    def push(self, item):
        self._items.append(item)
        return item

    def pop(self):
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        if not self._items:
            raise IndexError("peek at empty stack")
        return self._items[-1]

    def clear(self):
        self._items.clear()

    def to_list(self):
        return list(self._items)


def is_balanced(text):
    """Return True when every bracket in text is closed in the right order."""
    stack = Stack()
    openers = set(Stack.PAIRS.values())
    for char in text:
        if char in openers:
            stack.push(char)
        elif char in Stack.PAIRS:
            if not stack or stack.pop() != Stack.PAIRS[char]:
                return False
    return not stack


def evaluate_postfix(tokens):
    """Evaluate a postfix expression given as a list of tokens."""
    stack = Stack()
    for token in tokens:
        if token in ("+", "-", "*", "/"):
            right = stack.pop()
            left = stack.pop()
            if token == "+":
                stack.push(left + right)
            elif token == "-":
                stack.push(left - right)
            elif token == "*":
                stack.push(left * right)
            else:
                if right == 0:
                    raise ZeroDivisionError("division by zero in expression")
                stack.push(left / right)
        else:
            stack.push(float(token))
    if len(stack) != 1:
        raise ValueError("malformed expression")
    return stack.pop()
