class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval: (interval[0], -interval[1]))
        result = []
        while intervals:
            curr = intervals.pop(0)
            while intervals and curr[1] >= intervals[0][0]:
                curr = [min(curr[0], intervals[0][0]), max(curr[1], intervals[0][1])]
                intervals.pop(0)
            result.append(curr)
        return result

"""
Runtime: 92 ms
Memory Usage: 16 MB
"""


class SolutionOnBook:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        for i in sorted(intervals, key=lambda x: x[0]):
            print('i', i)
            if merged and i[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], i[1])
            else:
                merged += i,    # equivalent to merged += [i]
        return merged

"""
Runtime: 84 ms, faster than 78.86% of Python3 online submissions for Merge Intervals.
Memory Usage: 16.2 MB, less than 57.34% of Python3 online submissions for Merge Intervals.
"""