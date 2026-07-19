class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_start, new_end = newInterval
         
        left = 0
        while left < len(intervals) and new_start > intervals[left][1]:
            left += 1
        #now left is the index new_start should be placed
        if left == len(intervals):
            intervals.append(newInterval)
            return intervals
        new_start = min(new_start, intervals[left][0])
        right = left

        while right < len(intervals) and new_end >= intervals[right][0]:
            new_end = max(new_end, intervals[right][1])
            right += 1

        intervals[left: right] = [[new_start, new_end]]
        return intervals

