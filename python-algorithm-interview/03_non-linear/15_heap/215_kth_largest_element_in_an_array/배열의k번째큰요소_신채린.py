# 1번 풀이 (가장 빠름)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k-1]

# 2번 풀이 - heapq 모듈 이용
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = list() 
        for n in nums:
            heapq.heappush(heap, -n)
        for _ in range(k):
            heapq.heappop(heap)
        return -heapq.heappop(heap) 

# 파이썬 모듈은 최소 힙만 지원하므로 음수로 저장한 후, 
# 가장 낮은 수부터 추출해 부호를 변환하면 힙처럼 동작할 수 있따.

#3번 풀이 - heapq 모듈의 heapify 이용 
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        for _ in range(len(nums) - k):
            heapq.heappop(nums)
        return heapq.heappop(nums)


# 풀이 4 - heapq 모듈의 nlargest 이용
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]