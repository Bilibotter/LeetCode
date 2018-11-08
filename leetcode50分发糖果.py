class Solution:
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        a = []
        before = float('inf')
        for rate in ratings:
            if rate > before:
                a.append(a[-1]+1)
            else:
                a.append(1)
            before = rate
        r = 0
        accmul = 1
        before = float('inf')
        while a:
            num = a.pop()
            now = ratings.pop()
            if now > before:
                accumul+=1
            else:
                accumul = 1
            r += max(accumul, num)
            before = now
        return r
