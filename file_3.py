"""Simple sorting and searching helpers used for contribution testing."""


def insertion_sort(items):
    """Sort a list in ascending order using insertion sort."""
    result = list(items)
    for i in range(1, len(result)):
        current = result[i]
        j = i - 1
        while j >= 0 and result[j] > current:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = current
    return result


def selection_sort(items):
    """Sort a list in ascending order using selection sort."""
    result = list(items)
    n = len(result)
    for i in range(n - 1):
        smallest = i
        for j in range(i + 1, n):
            if result[j] < result[smallest]:
                smallest = j
        if smallest != i:
            result[i], result[smallest] = result[smallest], result[i]
    return result


def binary_search(sorted_items, target):
    """Return the index of target in a sorted list, or -1 if absent."""
    low = 0
    high = len(sorted_items) - 1
    while low <= high:
        middle = (low + high) // 2
        if sorted_items[middle] == target:
            return middle
        if sorted_items[middle] < target:
            low = middle + 1
        else:
            high = middle - 1
    return -1


def is_sorted(items):
    """Return True when the list is in non-decreasing order."""
    return all(items[i] <= items[i + 1] for i in range(len(items) - 1))


def main():
    sample = [9, 4, 7, 1, 8, 2, 6, 3, 5]
    by_insertion = insertion_sort(sample)
    print("insertion:", by_insertion)
    print("selection:", selection_sort(sample))
    print("sorted:", is_sorted(by_insertion), "| index of 6:", binary_search(by_insertion, 6))


if __name__ == "__main__":
    main()
