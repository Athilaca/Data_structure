class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

    
class Stack:
    def __init__(self):
        self.top=None 
          
    def push(self,data):
        new_node=Node(data)
        new_node.next=self.top
        self.top=new_node

    def pop(self):
        popped_item = self.top.data
        self.top =self.top.next 
        return popped_item

    def size(self):
        count = 0
        current = self.top
        while current:
            count += 1
            current = current.next
        return count
            
    def display(self):
        current=self.top
        while current:
            print(current.data)
            current=current.next 


    def is_empty(self):
        return self.top is None        

    def reverse_stack(self):
        temp = Stack()
        
        while not self.is_empty():
            item = self.pop()
            temp.push(item)

        self.top = temp.top
stack = Stack()

# Push some elements onto the stack

stack.push(10)
stack.push(20)
stack.push(30)
stack.pop()
stack.reverse_stack()            
stack.display()
