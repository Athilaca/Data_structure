class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class BinaryTree:
    def __init__(self):
        self.root=None
    # def insert(self,value):
    #     if self.root is None:
    #         self.root=Node(value)
    #     else:
    #         self._insert_recursive(value,self.root)

    # def _insert_recursive(self,value,current_node):
    #     if value<current_node.value:
    #         if current_node.left is None:
    #            current_node.left= Node(value)
    #         else:
    #             self._insert_recursive(value,current_node.left)

    #     else:
    #         if current_node.right is None:
    #             current_node.right=Node(value)
    #         else:
    #             self._insert_recursive(value,current_node.right)
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
    def delete(self, key):
            parent = None
            current_node = self.root

            while current_node is not None and current_node.value != key:
                parent = current_node
                if key < current_node.value:
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
            print(node.value, end=" ")
            self.inorder_traversal(node.left)
            self.inorder_traversal(node.right)
                
a=BinaryTree()
b=[100,200,]
for i in b:
    a.insert(i)

a.inorder_traversal(a.root)