class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self,size):
        self.size=size
        self.table=[None]*self.size

    def hash_function(self,key):
        return hash(key) % self.size

        
    def get(self, key):
        index = self.hash_function(key)
        current = self.table[index]

        # Search for the key in the linked list
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next

        # Key not found
        raise KeyError(f"Key '{key}' not found")
                   
    
    def display(self):
        for index in range(self.size):
            print(f"Bucket {index}: ", end="")
            current = self.table[index]

            while current is not None:
                print(f"({current.key}: {current.value})", end=" -> ")
                current = current.next

            print("None")
        
    
            
    def insert(self, key, value):
        index = self.hash_function(key)
        current = self.table[index]



        # Search for the key in the linked list
        while current is not None:
            if current.key == key:
                # Update the value if the key already exists
                current.value = value
                return
            current = current.next
        
        # If the key is not found, add a new node to the beginning of the linked list
        new_node = Node(key, value)
        new_node.next = self.table[index]
        self.table[index] = new_node        
    

hash_table = HashTable(10)
hash_table.insert("apple", 5)
hash_table.insert("banana", 10)
hash_table.insert("orange", 10)
hash_table.insert("orange",3)
hash_table.insert("apple", 8)  # Update value for existing key
hash_table.insert("grapes", 12)
print(hash_table.get("apple"))
print(hash_table.get("grapes"))  # Output: 8
print(f"Number of buckets in the custom hash table: {hash_table.size}")

hash_table.display()       


