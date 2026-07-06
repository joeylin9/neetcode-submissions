class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_start, new_end = newInterval

        def mergeEnd(i):
            while i < len(intervals):
                start, end = intervals[i]
                if new_end < start:
                    return intervals
                else: # new end still passes start, so need to merge
                    # case 1 between                        
                    if new_end<end or new_end == start:
                        intervals[i-1][1] = end
                        intervals.pop(i)
                        return intervals
                    # case 2 after end
                    else:
                        intervals.pop(i)
            return intervals

        def mergeStart():
            for i, interval in enumerate(intervals):
                start, end = interval
                if end >= new_start:
                    if new_start < start:
                        intervals.insert(i, newInterval)
                        if new_end < start: # new interval no overlap
                            return intervals
                        else:
                            return mergeEnd(i+1)
                    elif new_start >= start:
                        if end >= new_end: # completely merged
                            return intervals
                        else:
                            print('here')
                            intervals[i][1] = new_end
                            print(intervals)
                            print(i)
                            return mergeEnd(i+1)
            intervals.append(newInterval)
            return intervals
        
        return mergeStart()