class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, value):
        self.heap.append(value)
        self._heapify_up()

    def pop(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down()
        return root

    def peek(self):
        return self.heap[0] if self.heap else None

    def _heapify_up(self):
        index = len(self.heap) - 1
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] < self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:  
                break

    def _heapify_down(self):
        index = 0
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            smallest = index

            if (
                left_child_index < len(self.heap)
                and self.heap[left_child_index] < self.heap[smallest]
            ):
                smallest = left_child_index

            if (
                right_child_index < len(self.heap)
                and self.heap[right_child_index] < self.heap[smallest]
            ):
                smallest = right_child_index

            if smallest != index:
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                index = smallest
            else:
                break

# Example usage:
min_heap = MinHeap()
min_heap.push(4)
min_heap.push(8)
min_heap.push(2)
min_heap.push(5)

print("Min heap elements:")
while min_heap.heap:
    print(min_heap.pop())






