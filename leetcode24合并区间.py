# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """

        def k(inter):
            return inter.start

        if len(intervals) <= 1:
            return intervals

        intervals.sort(key=k)
        tup = intervals.pop(0)
        result = [tup]

        for tup in intervals:
            if result[-1].end >= tup.start:
                end = max(result[-1].end, tup.end)
                result[-1].end = end
            else:
                result.append(tup)

        return result

