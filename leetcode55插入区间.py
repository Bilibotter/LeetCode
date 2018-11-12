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
    
# 重新失去人生意义，98.6%的大神解
class Solution:
    def insert(self, intervals, newInterval):
        head = newInterval.start
        tail = newInterval.end
        left = [interval for interval in intervals if interval.end < head]
        right = [interval for interval in intervals if interval.start > tail]
        if len(left) + len(right) < len(intervals):
            head = min(intervals[len(left)].start, head)
            tail = max(intervals[-len(right)-1].end, tail)
        return left + [Interval(head, tail)] + right
