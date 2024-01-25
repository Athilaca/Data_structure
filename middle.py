class stack():
    def __init__(self): 
      self.items=[]

    def push(self,value):
       self.items.append(value)

    def pop(self):
       return self.items.pop()
    
    def is_empty(self):
       return len(self.items)==0
    
    def delete_middle(self):
        temp=stack()
       
        middle=len(self.items)//2
        for _ in range(middle):
             
            temp.push(self.pop())
        self.pop()
       

        self.push(temp.pop())    
       

    def display(self):
      print(self.items)


my_stack=stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)
my_stack.push(5)
my_stack.delete_middle()
my_stack.display()       