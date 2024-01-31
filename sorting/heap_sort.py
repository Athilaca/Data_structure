def heapify(arr, n, i):
    largest = i  # Initialize largest as the root
    left_child = 2 * i + 1  # Left child index
    right_child = 2 * i + 2  # Right child index

    # Compare the root with the left child
    if left_child < n and arr[left_child] > arr[largest]:
        largest = left_child

    # Compare the root with the right child
    if right_child < n and arr[right_child] > arr[largest]:
        largest = right_child

    # Swap if needed and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from the heap in sorted order
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap the root with the last element
        heapify(arr, i, 0)  # Heapify the reduced heap

    return arr


# Example usage
input_array = [12, 11, 13, 5, 6, 7]
sorted_array = heap_sort(input_array)
print("Sorted array:", sorted_array)

