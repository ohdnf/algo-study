class Node:
    
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = dict()


class Trie:

    def __init__(self):
        self.root = Node(None)
       

    def insert(self, word: str) -> None:
        c_node = self.root
        for c in word:
            if c not in c_node.children:
                c_node.children[c] = Node(c)
            c_node = c_node.children[c]
        c_node.data = word
        
        
    def search(self, word: str) -> bool:
        c_node = self.root
        
        for c in word:
            if c in c_node.children:
                c_node = c_node.children[c]
            else:
                return False
            
        if c_node.data != None:
            return True

    def startsWith(self, prefix: str) -> bool:
        c_node = self.root
        subtrie = None
        
        for c in prefix:
            if c in c_node.children:
                c_node = c_node.children[c]
                subtrie = c_node
            else:
                return False
        return True

'''
Runtime: 184 ms, faster than 54.99% of Python3 online submissions for Implement Trie (Prefix Tree).
Memory Usage: 33.1 MB, less than 25.54% of Python3 online submissions for Implement Trie (Prefix Tree).
'''