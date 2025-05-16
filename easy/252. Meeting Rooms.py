from typing import List


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        end = 0
        for meet in intervals:
            if meet.start - end < 0:
                return False
            end = meet.end
        return True


a = Solution()
intervals = [Interval(0, 8), Interval(8, 10)]
intervals2 = [Interval(5, 8), Interval(9, 15)]
intervals3 = [Interval(0, 30), Interval(5, 10), Interval(15, 20)]
print(a.can_attend_meetings(intervals3))
