class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class Doubly:
    def __init__(self):
        self.head=None
        self.tail=None

    def append(self,data):
        new_node=Node(data)
        if self.head is  None:
            self.head=new_node
        else:
            new_node.prev=self.tail
            self.tail.next=new_node

        self.tail=new_node

    def display(self):
        current=self.head
        while current:
            print(current.data,end=" ") 
            current=current.next   
        print()

    def display_reverse(self):
        current=self.tail
        while current:
            print(current.data,end=" ")
            current=current.prev

    def delete(self, data):
        current = self.head
        if self.head is None:
            print("empty")
            return
        if current.data == data:
            self.head = current.next
            return  
        
        while current is not None:
            if current.data == data:
                current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev  # Update tail if deleting the last node
                return
            current = current.next

        
    def before(self,x,new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        if self.head.data == x:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            return

        current = self.head
        while current:
            if current.data == x:
                break
            current = current.next
        if not current:
            print(f"Node with value {x} not found in the list.")
            return

        new_node.next=current
        new_node.prev=current.prev
        current.prev.next=new_node
        current.prev=new_node  

       
        # new_node.next=current.next
        # new_node.prev=current
        # if current.next:
        #    current.next.prev=new_node
        # current.next=new_node
   
linked=Doubly()
linked.append(1)
linked.append(2)
linked.append(3)
linked.append(4)
linked.append(5)
linked.before(5,1)
# linked.delete(5)
linked.display()