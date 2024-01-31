class MaxHeap:
    def __init__(self):
        self.heap = []

    def push(self, value):
        self.heap.append(value)
        self._heapify_up()

    def remove(self):
        if not self.heap:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down()

        return max_value


    def peek(self):
        return self.heap[0] if self.heap else None

    def _heapify_up(self):
        index = len(self.heap) - 1 #the index of element added (in array we take 0th position)
        while index > 0:
            parent_index = (index - 1) // 2 # after adding find the root of that using (i-1/2 ) equation
            if self.heap[index] > self.heap[parent_index]: # in max parent (root) should be greater otherwise swap
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index 
                #after swapping the inserting element changes it position to parent _index so again find the root until it become in the crct position where root(parent) become higher
                
            else:
                break

    def _heapify_down(self):
        index = 0
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            largest = index

            if (
                left_child_index < len(self.heap)  
                and self.heap[left_child_index] > self.heap[largest]
            ):
                largest = left_child_index

            if (
                right_child_index < len(self.heap)
                and self.heap[right_child_index] > self.heap[largest]
            ):
                largest = right_child_index

            if largest != index:
                self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
                index = largest
            else:  
                break
    

    

# Example usage:
max_heap = MaxHeap()
max_heap.push(4)
max_heap.push(8)
max_heap.push(2)
max_heap.push(5)
max_heap.push(6)
max_heap.push(1)
# max_heap.asc_sort()
print("Max heap elements:")
while max_heap.heap:
    print(max_heap.remove())
