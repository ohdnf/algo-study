class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        print(intervals)
        
        # a,b 머지
        result = [intervals[0][:]]
        for dst in range(1, len(intervals)):
            if result[-1][1] >= intervals[dst][0]:
                result[-1][1] = max(result[-1][1], intervals[dst][1])
            else:
                result.append(intervals[dst][:])
        return result
# Runtime: 92 ms, faster than 33.83% of Python3 online submissions for Merge Intervals.
# Memory Usage: 16.2 MB, less than 57.80% of Python3 online submissions for Merge Intervals.
