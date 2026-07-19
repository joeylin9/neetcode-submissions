class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[0], x[1]))

        count = 0
        start, end = intervals[0]
        j = 1
        while j < len(intervals):
            cur_start, cur_end = intervals[j]
            if end <= cur_start: # no overlap
                start, end = cur_start, cur_end
            else: #overlap
                end = min(end, cur_end)
                count += 1
            j += 1
        return count
