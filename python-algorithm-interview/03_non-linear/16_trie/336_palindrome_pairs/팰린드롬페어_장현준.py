class TrieNode:
    def __init__(self):
        self.word = 0
        self.children = dict()

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def insert(self, idx: int, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.word = idx
        
    
    def searchPalindrome(self, i: int, j: int, word: str) -> bool:
        node = self.root
        if node.word == i:
            # 예외 케이스
            target = j
        else:
            target = i
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
            if node.word == target and target == i:
                node = self.root
                target = j
        if node.word == target:
            return True
        else:
            return False
        

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        answer = []
        trie = Trie()
        # 1234, 321 => 1234321
        for i, word in enumerate(words):
            trie.insert(i+1, word)
            
        for i, word1 in enumerate(words):
            for j, word2 in enumerate(words):
                if i == j:
                    continue
                word = word1 + word2
                if trie.searchPalindrome(i+1, j+1, word[::-1]):
                    answer.append([i, j])
        return answer

'''
78/134에서 초과나는 코드
'''

class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.word_id = -1
        self.palindrome_word_ids = []

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    @staticmethod
    def is_palindrome(word: str) -> bool:
        return word[::] == word[::-1]
    
    def insert(self, index, word) -> None:
        node = self.root
        for i, char in enumerate(reversed(word)):
            if self.is_palindrome(word[:len(word)-i]): # abaaba => i=0 : abaaba, i=3 : aba는 스스로 펠린드롬단어
                node.palindrome_word_ids.append(index)
            node = node.children[char]
            node.val = char # 사용하진 않는것 같음
        node.word_id = index # 단어 => T/F 아닌 0 <= 정수로 표현
    
    def search(self, index, word) -> List[List[int]]:
        result = []
        node = self.root
        # now_word = "" => 루트부터 현재까지 탐색한 단어
        while word:
            # 판별로직3
            if node.word_id >= 0 and self.is_palindrome(word): # 팰린드롬 된 단어 => now_word + word + now_word
                result.append([index, node.word_id])
            if not word[0] in node.children:
                return result
            node = node.children[word[0]]
            # now_word += word[0]
            word = word[1:]
        # 이제 now_word는 입력받은 word와 동일
        # 판별로직1
        if node.word_id >=0 and node.word_id != index: # 팰린드롬 된 단어 => now_word + now_word, and 자기자신과 결합 X
            result.append([index, node.word_id])
        
        # 판별로직2
        for palindrome_word_id in node.palindrome_word_ids: # 팰린드롬 된 단어 => now_word + palindrome_word_ids의 단어 + now_word
            result.append([index, palindrome_word_id])
        
        return result

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        trie = Trie()
        
        for i, word in enumerate(words):
            trie.insert(i, word)
        
        results = []
        for i, word in enumerate(words):
            results.extend(trie.search(i, word))

        return results
'''
교재 코드 베낀거
Runtime: 1420 ms, faster than 8.40% of Python3 online submissions for Palindrome Pairs.
Memory Usage: 21.3 MB, less than 8.92% of Python3 online submissions for Palindrome Pairs.
'''