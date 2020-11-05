'''
Given two integers n and k,
return all possible combinations of k numbers out of 1 ... n.
'''


class Solution:
    def combine(self, n: int, k: int):
        result = []
        max_num = n - k + 2

        def get_combi(i, j, num_list):
            if j == k:
                result.append(num_list[:])
                return
            for num in range(i, max_num + j):
                num_list[j] = num
                get_combi(num + 1, j + 1, num_list)

        get_combi(1, 0, [0] * k)
        return result

a = Solution()
print(a.combine(4, 2))

from itertools import combinations