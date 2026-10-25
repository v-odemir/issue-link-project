"""Bubble sort implementation used for contribution testing."""


def bubble_sort(items):
    """Sort a list in ascending order using bubble sort. Returns a new list."""
    result = list(items)
    n = len(result)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        if not swapped:
            break
    return result


def main():
    sample = [9, 4, 7, 1, 8, 2, 6, 3, 5]
    print("bubble:", bubble_sort(sample))


if __name__ == "__main__":
    main()
