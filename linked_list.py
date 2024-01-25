class Node:
    def __init__(self,data) :
        self.data=data
        self.next=None
        self.prev=None
 
class Simplylinked_list:
    def __init__(self):
        self.head=None
        self.tail=None


    def append(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
           self.tail.next=new_node  

        self.tail=new_node
        

    def display(self):

        current=self.head
        while current:
            print(current.data, end=" ")
            current=current.next 
        print()       

    def array_to_linkedlist(self,arr):
        for item in arr:
            self.append(item)



    def prepend(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
        if self.tail is None:
            self.tail=new_node
    
    def add_before(self,x,node):
        current=self.head
        if current.data==x:
            new_node =Node(node)
            new_node.next=self.head
            self.head=new_node
            return
        while current.next is not None:
            if current.next.data==x:
                break
            current=current.next
        new_node=Node(node)
        new_node.next=current.next
        current.next=new_node
      


    def add_after(self,x,data):
        current=self.head
        while current.next is not None:
            if current.data==x:
                break
            current=current.next
        new_node=Node(data)
        new_node.next=current.next
        current.next=new_node       


    def reverse_linked_list(self):
        prev = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head=prev
        return prev       

    


    def remove_duplicates(self):
        if not self.head:
          return  
        current=self.head

        while current  and current.next:
            if current.data == current.next.data:
                current.next =current.next.next
            else:
                current=current.next           

    def middle(self):
        if self.head is None:
            return None
        slow=self.head
        fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        print(slow.data)
        return slow.data
    
    def delete(self,x):
        current=self.head
        while current.next is not None:
            if current.next.data==x:
                break
            current=current.next
        if current is not None:
            current.next=current.next.next

    
    def delete_before(self,x):
        current=self.head
        while current.next.next is not None:
            if current.next.next.data==x:
                break
            current=current.next
        current.next=current.next.next  

    def delete_after(self,x):    
        current=self.head
        while current.next.next is not None:
            if current.data==x:
                break
            current=current.next
        current.next=current.next.next    


    def merge_linked_lists(self,list1,list2):
            if not list1:
                return list2
            if not list2:
                return list1
            current = list1.head
            while current.next:
                current = current.next
            current.next = list2.head

            return list1
    
    def reverse(self):
        prev = None
        current = self.head
        self.tail = current  # Update the tail to the new head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev  
       
linked_list=Simplylinked_list()
l1=Simplylinked_list()

array=[4,5,6,7,5,8,9]
new=[2,7,9,5,4,3,9]
linked_list.array_to_linkedlist(array)
# l1.array_to_linkedlist(new)
# new_linked_list=l1.merge_linked_lists(linked_list,l1)
# new_linked_list.delete_before(9)
linked_list.add_before(4,1)
linked_list.delete_after(8)
# linked_list.reverse()
linked_list.display()


