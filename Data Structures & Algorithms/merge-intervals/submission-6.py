class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals

        intervals.sort(key=lambda x: x[0])

        ans = []
        start, end = intervals[0]
        j = 1
        while j < len(intervals):
            if end >= intervals[j][0]: #overlaps
                end = max(intervals[j][1], end)
            else: # no overlap
                ans.append([start, end])
                start, end = intervals[j]
            j += 1
        ans.append([start, end])
        return ans
