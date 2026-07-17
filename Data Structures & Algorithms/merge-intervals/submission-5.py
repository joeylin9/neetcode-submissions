class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        ans = []
        current = intervals[0]

        for i in range(1, len(intervals)):
            if current[1] < intervals[i][0]:
                # No overlap
                ans.append(current)
                current = intervals[i]
            else:
                # Overlap: extend the current interval
                current[1] = max(current[1], intervals[i][1])

        ans.append(current)
        return ans