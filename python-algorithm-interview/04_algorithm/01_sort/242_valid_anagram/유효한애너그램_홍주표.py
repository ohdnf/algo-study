class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram = dict()
        for c in s:
            anagram[c] = anagram.get(c, 0) + 1
        for c in t:
            if c in anagram:
                anagram[c] -= 1
            else:
                return False
        for k, v in anagram.items():
            if v != 0:
                return False
        return True

"""
Runtime: 52 ms, faster than 47.07% of Python3 online submissions for Valid Anagram.
Memory Usage: 14.4 MB, less than 74.88% of Python3 online submissions for Valid Anagram.
"""

