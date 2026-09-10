"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # sort by start time
        intervals.sort(key = lambda i : i.start)

        #iterate through starting from second item in list
        for i in range(1, len(intervals)):
            i1 = intervals[i - 1]
            i2 = intervals[i]
        # then check if i1.end > i2.start, return False
            if i1.end > i2.start:
                return False
        return True