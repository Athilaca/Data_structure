class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear=None
    def enqueue(self, data):
        new_node = Node(data)
        if not self.rear:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if not self.front:
            return None
        else:
            removed_item = self.front.data
            self.front = self.front.next
            if not self.front:
                self.rear = None
            return removed_item

    def size(self):
        count = 0
        current = self.front
        while current:
            count += 1
            current = current.next
        return count

    def display(self):
        current = self.front
        while current:
            print(current.data)
            current = current.next

# Example usage:
queue = Queue()

queue.enqueue(40)
queue.enqueue(50)
queue.enqueue(60)
dequeued_item = queue.dequeue()
print("Dequeued Item:", dequeued_item)
print("Queue Size:", queue.size())
print("Queue Elements:")
queue.display()
