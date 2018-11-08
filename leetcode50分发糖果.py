class Solution:
    def candy(self, ratings):
        my = [1]* len(ratings)
        for i in range(1,len(ratings)):
            if ratings[i] > ratings[i-1]:
                my[i] = my[i-1]+1
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1] and my[i] <= my[i+1]:
                my[i] = my[i+1] + 1
        return sum(my)
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
