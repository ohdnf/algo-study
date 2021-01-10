class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        heapq.heapify(nums)
        
        while len(nums) > k:
            heapq.heappop(nums)
        
        return heapq.heappop(nums)

'''
Runtime: 100 ms, faster than 22.26% of Python3 online submissions for Kth Largest Element in an Array.
Memory Usage: 15 MB, less than 67.41% of Python3 online submissions for Kth Largest Element in an Array.
'''