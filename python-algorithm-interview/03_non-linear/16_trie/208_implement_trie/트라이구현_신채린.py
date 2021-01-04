class Trie:

    def __init__(self):
        self.isWord = False
        self.children = {}
        

    def insert(self, word: str) -> None:
        node = self
        for w in word:
            if w not in node.children:
                node.children[w] = Trie()
            node = node.children[w]
        
        node.isWord = True
    def search(self, word: str) -> bool:
        node = self
        for w in word:
            if w not in node.children:
                return False
            node = node.children[w]
        
        return node.isWord
        

    def startsWith(self, prefix: str) -> bool:
        node = self
        for w in prefix:
            if w not in node.children:
                return False
            node = node.children[w]
        
        return True
