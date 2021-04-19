from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return sorted(points, key=lambda p: p[0] ** 2 + p[1] ** 2)[:k]

"""
Runtime: 640 ms, faster than 81.99% of Python3 online submissions for K Closest Points to Origin.
Memory Usage: 19.8 MB, less than 73.59% of Python3 online submissions for K Closest Points to Origin.
"""
