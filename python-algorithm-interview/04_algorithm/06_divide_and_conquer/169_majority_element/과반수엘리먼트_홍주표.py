from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        element, appears = counter.most_common(1)[0]
        if appears > (len(nums) // 2):
            return element
        return None


class SolutionSorting:
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]


class SolutionDivideAndConquer:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]

        first = self.majorityElement(nums[:len(nums) // 2])
        second = self.majorityElement(nums[len(nums) // 2:])

        return [second, first][nums.count(first) > len(nums) // 2]
