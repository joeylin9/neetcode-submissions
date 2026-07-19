"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: (x.start, x.end))

        earliest = []
        rooms = 0

        for interval in intervals:
            if earliest and earliest[0] <= interval.start:
                # Reuse an available room
                heapq.heappop(earliest)
            else:
                # Every room is occupied
                rooms += 1

            heapq.heappush(earliest, interval.end)

        return rooms
