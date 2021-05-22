class Solution:
    from heapq import heappop, heappush
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        lst = []
        for i in range(k):
            heappush(lst, (-nums[i], i))
        answer = [-lst[0][0]]
        
        for i in range(k, len(nums)):
            heappush(lst, (-nums[i], i))
            while lst[0][1] <= i-k:
                heapgpop(lst)
            answer.append(-lst[0][0])
        return answer
'''
Runtime: 1940 ms, faster than 29.58% of Python3 online submissions for Sliding Window Maximum.
Memory Usage: 38.5 MB, less than 6.90% of Python3 online submissions for Sliding Window Maximum.
'''