class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        tree = [0]
        
        # insert
        for num in nums:
            tree.append(num)
    
            src = len(tree)-1
            dst = src // 2
            while dst != 0:
                
                # MinHeap
                if tree[src] >= tree[dst]:
                    break
                tree[src], tree[dst] = tree[dst], tree[src]
                src = dst
                dst = src // 2
        # delete
        step = 0
        k = len(tree) - k # MinHeap에서 k번째 큰 값
        while True:
            step += 1
            number = tree[1]
            if step == k:
                return number
            tree[1] = tree.pop()
            
            src = 1
            while True:
                dst = src
                if 2*src < len(tree) and tree[dst] > tree[2*src]:
                    dst = 2*src
                if 2*src+1 < len(tree) and tree[dst] > tree[2*src+1]:
                    dst = 2*src+1
                if dst == src:
                    break
                tree[src], tree[dst] = tree[dst], tree[src]
                src = dst
'''
Runtime: 184 ms, faster than 16.73% of Python3 online submissions for Kth Largest Element in an Array.
Memory Usage: 15.2 MB, less than 41.36% of Python3 online submissions for Kth Largest Element in an Array.
'''

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        lst = []
        for num in nums:
            heapq.heappush(lst, num)
        for _ in range(len(nums)-k):
            heapq.heappop(lst)
        return heapq.heappop(lst)
'''
Runtime: 112 ms, faster than 20.65% of Python3 online submissions for Kth Largest Element in an Array.
Memory Usage: 15.2 MB, less than 41.36% of Python3 online submissions for Kth Largest Element in an Array.
'''