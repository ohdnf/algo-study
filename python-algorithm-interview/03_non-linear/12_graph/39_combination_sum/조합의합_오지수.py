class Solution:
    def combinationSum(self, candidates, target):
        candidates.sort()
        result = []

        def get_sum(nums_list, index, remain_number):
            if not remain_number:
                result.append(nums_list)
                return

            for i in range(index, len(candidates)):
                if candidates[i] <= remain_number:
                    get_sum(nums_list + [candidates[i]], i, remain_number - candidates[i])
                else:
                    break
        get_sum([], 0, target)
        return result

a = Solution()
b = a.combinationSum([2,3,6,7], 7)
print(b)