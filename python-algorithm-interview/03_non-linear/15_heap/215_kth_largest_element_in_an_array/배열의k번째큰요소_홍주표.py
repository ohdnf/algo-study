# Solution 1
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq as h
        length = len(nums)
        heap = []
        while nums:
            h.heappush(heap, nums.pop())
        for _ in range(length-k):
            h.heappop(heap)
        return h.heappop(heap)

"""
Runtime: 72 ms, faster than 33.00% of Python3 online submissions for Kth Largest Element in an Array.
Memory Usage: 14.8 MB, less than 71.96% of Python3 online submissions for Kth Largest Element in an Array.
"""

# Solution 2
# 직접 heap 구조 만들어 보기
