class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class BinaryTree:
    def __init__(self):
        self.root=None
        self.array=[]

    def insert(self,value):
        new_node=Node(value)
        if self.root is None:
            self.root=new_node
        else:
            current = self.root
            
            while True:
                if value<current.value:
                    if current.left is None:
                        current.left=new_node
                        break
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right=new_node
                        break
                    else:
                        current = current.right
    
    def delete(self, target):
            parent = None
            current_node = self.root

            while current_node is not None and current_node.value != target:
                parent = current_node
                if target < current_node.value:
                    current_node = current_node.left
                else:
                    current_node = current_node.right

            if current_node is None:
                return

            if current_node.left is None:
                # Node with one child or no child
                if current_node == self.root:
                    self.root = current_node.right
                elif parent.left == current_node:
                    parent.left = current_node.right
                else:
                    parent.right = current_node.right

            elif current_node.right is None:
                # Node with one child (left)
                if current_node == self.root:
                    self.root = current_node.left
                elif parent.left == current_node:
                    parent.left = current_node.left
                else:
                    parent.right = current_node.left
            else:
                # Node with two children
                successor_parent = current_node
                successor = current_node.right


                while successor.left is not None:
                    successor_parent = successor
                    successor = successor.left

                current_node.value = successor.value

                if successor_parent.left == successor:
                    successor_parent.left = successor.right
                else:
                    successor_parent.right = successor.right



    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.value, end=" ")
            self.inorder_traversal(node.right)        
    

    def is_bst(self,node, prev=[None]):
        if not node:
            return True

        # Check the left subtree
        if not self.is_bst(node.left, prev):
            return False

        # Check the current node
        if prev[0] is not None and node.value < prev[0].value:
            return False
        prev[0] = node

        # Check the right subtree
        return self.is_bst(node.right, prev)             

    def find_height(self,node):
        if node is None:
          return 0

        left_height=self.find_height(node.left)
        right_height=self.find_height(node.right)
        return max(left_height,right_height)+1

    
    def find_closest_value(node,target):
        if node is None:
            return
        closest=node.value
        if abs(target-node.value)<abs(target-closest):
            closest=node.value
        




c=BinaryTree()
# b=[200,190,215,188,193,209,220,186,189,191,195,208,210,218,230,198,194]
b=[6,2,7,4,9]

for i in b:
    c.insert(i)

c.delete(220)
  
c.inorder_traversal(c.root)
a=c.find_height(c.root)
print(a)

result = c.is_bst(c.root)   
print("Is the tree a BST?", result)