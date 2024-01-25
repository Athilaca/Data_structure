#circular linkedlist implementation

class Node:
    def __init__(self,data) :
        self.data=data
        self.next=None
        self.prev=None
 
class circular_linked_list:
    def __init__(self):
        self.head=None
        self.tail=None


    def append(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            new_node.next = self.head
        else:
           self.tail.next=new_node  
           new_node.next = self.head
        self.tail=new_node
        

    def display(self):
    
        current=self.head
        while current:
            print(current.data, end=" ")
            current=current.next 
            if current == self.head:
                break
        print()       

linked_list = circular_linked_list()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.display()