class MyStack:

    def __init__(self):
       self.queue1 = []
       self.queue2 = []
 

    def push(self, x):
        self.queue1.append(x)
        while self.queue2:
            self.queue1.append(self.queue2.pop(0))

       
        self.queue1, self.queue2 = self.queue2, self.queue1
        

    def pop(self):
        if not self.queue2:
            raise IndexError("Stack is empty")

        return self.queue2.pop(0)

        

    def top(self):
        if not self.queue2:
            raise IndexError("Stack is empty")

        return self.queue2[0]
        

    def empty(self):
        return not self.queue2
    
    def display(self):
        print(self.queue2)
        

obj = MyStack()
obj.push(7)
obj.push(8)
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()
obj.display()