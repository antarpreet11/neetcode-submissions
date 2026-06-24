"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)

        for i in range(1, len(intervals)):
            x1 = intervals[i - 1]
            x2 = intervals[i]

            if x1.end > x2.start:
                return False
        return True
