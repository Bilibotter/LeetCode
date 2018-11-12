# 击败96.86%
class Solution:
    def insert(self, intervals, newInterval):
        start = newInterval.start
        end = newInterval.end
        ans = []
        for i, interval in enumerate(intervals):
            if interval.end < start:
                ans.append(interval)
            else:
                start = min(interval.start, start)
                if end < interval.start:
                    ans.append(Interval(start, end))
                    ans.extend(intervals[i:])
                    return ans
                elif end <= interval.end:
                    ans.append(Interval(start, interval.end))
                    ans.extend(intervals[i+1:])
                    return ans
        ans.append(Interval(start, end))
        return ans
