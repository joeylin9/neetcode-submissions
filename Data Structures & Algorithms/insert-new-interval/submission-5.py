class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_start, new_end = newInterval
        n = len(intervals)

        i = 0
        # find merge start
        while i < n and intervals[i][1] < new_start:
            i += 1

        j = i
        # find merge end
        while j < n and intervals[j][0] <= new_end:
            new_start = min(new_start, intervals[j][0])
            new_end = max(new_end, intervals[j][1])
            j += 1

        # replace the whole overlapped block once
        intervals[i:j] = [[new_start, new_end]]
        return intervals