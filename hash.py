class Hashtable:
    def __init__(self,size):
        self.size=size
        self.table=[None]*self.size

    def hash_function(self,key):
        return hash(key) % self.size

    def insert(self,key,value):
        index=self.hash_function(key)
        self.table[index]=(key,value)

    def display(self):
        for i, bucket in enumerate(self.table):
            if bucket is not None:
                print(f"Bucket {i}: {bucket}")

    
        


hash_table=Hashtable(10)
hash_table.insert('Apple',1)
hash_table.insert('Apple',4)
hash_table.display()

