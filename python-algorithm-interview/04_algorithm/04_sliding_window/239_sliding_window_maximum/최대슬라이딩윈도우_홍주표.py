from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = deque()
        output = []
        for i, n in enumerate(nums):
            while window and nums[window[-1]] < n:
                window.pop()
            window.append(i)
            if window[0] == i - k:
                window.popleft()
            if i >= k - 1:
                output.append(nums[window[0]])
        return output

"""
Runtime: 1668 ms, faster than 90.20% of Python3 online submissions for Sliding Window Maximum.
Memory Usage: 29.7 MB, less than 82.62% of Python3 online submissions for Sliding Window Maximum.
"""
