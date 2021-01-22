class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        result = []
        tmp_arr = intervals.pop(0)
        while intervals:
            cur_arr = intervals.pop(0)
            if tmp_arr[1] >= cur_arr[0]:
                if tmp_arr[1] < cur_arr[1]:
                    tmp_arr[1] = cur_arr[1]
            else:
                result.append(tmp_arr)
                tmp_arr = cur_arr
        result.append(tmp_arr)
        return result

'''
Runtime: 76 ms, faster than 97.60% of Python3 online submissions for Merge Intervals.
Memory Usage: 16.2 MB, less than 57.71% of Python3 online submissions for Merge Intervals.
'''