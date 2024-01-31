class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root 
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True                  

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False  
            node = node.children[char]
        return node.is_end_of_word

    def starts_with_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True    

    def display_trie(self):
        stack = [(self.root, "")]
        
        while stack:
            current_node, prefix = stack.pop()
            
            if current_node.is_end_of_word:
                print(prefix)

            for char, child_node in current_node.children.items():
                stack.append((child_node, prefix + char))

  




# Example Usage
trie = Trie()

# Insert words into the trie
trie.insert("apple")
trie.insert("app")
trie.insert("apricot")
# print(trie.search("apple"))  # True
# print(trie.search("app"))    # True
# print(trie.search("apricot")) # True
# print(trie.search("banana"))  # False

# # Check if a prefix exists in the trie
# print(trie.starts_with_prefix("ap"))  # True
# print(trie.starts_with_prefix("ban")) # False
# # Display the Trie using while loop
# print("Trie Structure:")
trie.display_trie()
