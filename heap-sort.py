"""Heap sort implementation used for contribution testing."""


def _sift_down(items, start, end):
    """Move the value at start down until the subtree rooted there is a max-heap."""
    root = start
    while True:
        child = 2 * root + 1
        if child > end:
            break
        if child + 1 <= end and items[child] < items[child + 1]:
            child += 1
        if items[root] < items[child]:
            items[root], items[child] = items[child], items[root]
            root = child
        else:
            break


def heap_sort(items):
    """Sort a list in ascending order using heap sort. Returns a new list."""
    result = list(items)
    n = len(result)
    for start in range(n // 2 - 1, -1, -1):
        _sift_down(result, start, n - 1)
    for end in range(n - 1, 0, -1):
        result[0], result[end] = result[end], result[0]
        _sift_down(result, 0, end - 1)
    return result


def main():
    sample = [9, 4, 7, 1, 8, 2, 6, 3, 5]
    print("heap:", heap_sort(sample))


if __name__ == "__main__":
    main()
