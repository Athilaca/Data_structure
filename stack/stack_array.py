class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from an empty stack")

    def size(self):
        return len(self.items)
    
    def display(self):
        print("Stack:", self.items)

    def remove_even_numbers(self,stack):
        if not self.is_empty():
            current = self.pop()
            self.remove_even_numbers(stack)  # Recursive call before checking and pushing

            if current % 2 != 0:
                self.push(current)

    def remove_duplicates(self):
        a=[]
        temp=Stack()
        while not self.is_empty():
            current=self.pop()
            if current not in a:
                a.append(current)
                temp.push(current)
        while not temp.is_empty():
            self.push(temp.pop())

    def reverse_stack(self):
        temp = Stack()
        
        while not self.is_empty():
            item = self.pop()
            temp.push(item)

        self.items = temp.items

    def power_of_two(self,n):
        self.push(1) 
        for i in range(n):
            a=self.peek()
            self.push(a*2)

# Example usage with display
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(2)
stack.push(4)
stack.push(3)
stack.power_of_two(5)
print("Original Stack:")
stack.display()

# stack.remove_duplicates()

# print("Stack after removing duplicates:")
stack.reverse_stack()
stack.display()
