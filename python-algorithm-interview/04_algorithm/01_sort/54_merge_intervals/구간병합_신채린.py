class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        sorted(intervals, key = lambda x:x[0])
        for i in intervals:
            if merged and i[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], i[1])
            else:
                merged.append(i)
        return merged