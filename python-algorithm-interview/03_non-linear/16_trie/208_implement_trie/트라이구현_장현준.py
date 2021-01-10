class TrieNode:
    def __init__(self):
        self.word = False
        self.children = dict()

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]

        node.word = True
        

    def search(self, word: str) -> bool: # 단어의 유무
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.word
        

    def startsWith(self, prefix: str) -> bool: # 단어의 유무가 아닌, 일부
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

'''
Runtime: 216 ms, faster than 26.99% of Python3 online submissions for Implement Trie (Prefix Tree).
Memory Usage: 32.3 MB, less than 36.27% of Python3 online submissions for Implement Trie (Prefix Tree).
'''