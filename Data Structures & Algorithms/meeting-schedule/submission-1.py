"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
            
        intervals.sort(key = lambda x: x.start)
        _, e = intervals[0].start, intervals[0].end
        j = 1
        while j < len(intervals):
            cur_s, cur_e = intervals[j].start, intervals[j].end
            if e > cur_s:
                return False
            else:
                e = cur_e
            j+=1
        return True