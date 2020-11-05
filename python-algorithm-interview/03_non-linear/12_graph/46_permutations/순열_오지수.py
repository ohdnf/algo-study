class Solution:
    def permute(self, nums):
        result = []

        def get_permu(index, nums_list):
            if index == len(nums):
                result.append(nums_list[:])
                return
            for i in range(index, len(nums)):
                nums_list[index], nums_list[i] = nums_list[i], nums_list[index]
                get_permu(index+1, nums_list)
                nums_list[i], nums_list[index] = nums_list[index], nums_list[i]

        get_permu(0, nums)
        return result


a = Solution()
a.permute(nums = [1, 2, 3])