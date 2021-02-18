class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]
        max_length = len(max(nums, key=len))
        dict_nums = {num: num + '0' * (max_length - len(num)) for num in nums}
        largest = [k for k, v in sorted(dict_nums.items(), key=lambda item: item[1], reverse=True)]
    
        return ''.join(largest)

"""
Wrong Answer
Input [111311, 1113]
Output 1113111113
Expected 1113111311
"""



class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        return str(int(''.join(sorted(list(map(str, nums)), key=lambda n: n*10, reverse=True))))

"""
Runtime: 36 ms, faster than 82.75% of Python3 online submissions for Largest Number.
Memory Usage: 14.3 MB, less than 61.16% of Python3 online submissions for Largest Number.
"""


# 교재 해설
class Solution:
    @staticmethod
    def to_swap(n1: int, n2: int) -> bool:
        return str(n1) + str(n2) < str(n2) + str(n1)
    def largestNumber(self, nums: List[int]) -> str:
        i = 1
        while i < len(nums):
            j = i
            while j > 0 and self.to_swap(nums[j - 1], nums[j]):
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                j -= 1
            i += 1

        return str(int(''.join(map(str, nums))))