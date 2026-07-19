"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0

        intervals.sort(key = lambda x: (x.start, x.end))
        for i in intervals:
            print((i.start, i.end))

        cur_end = intervals[0].end
        earliest = [cur_end]
        heapq.heapify(earliest)
        j = 1
        rooms = 1
        while j < len(intervals):
            start, end = intervals[j].start, intervals[j].end
            heapq.heappush(earliest, end)
            if cur_end > start and earliest[0] > start:
                rooms += 1
                cur_end = end
            else:
                heapq.heappop(earliest)
                cur_end = end
            j += 1
        return rooms
