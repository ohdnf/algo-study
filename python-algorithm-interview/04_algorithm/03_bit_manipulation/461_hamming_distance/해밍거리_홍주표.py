class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        answer = 0
        z = x ^ y
        while z > 1:
            answer += z % 2
            z //= 2
        answer += z
        return answer

"""
Runtime: 32 ms, faster than 52.16% of Python3 online submissions for Hamming Distance.
Memory Usage: 14.2 MB, less than 74.19% of Python3 online submissions for Hamming Distance.
"""

# One-line Code
class SolutionOneLine:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x^y).count('1')

# Faster (28ms)
class SolutionOthers(object):
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        count = 0
        for _ in range(32):
            count += xor & 1
            xor = xor >> 1
        return count
