# 凡人解
class Solution:
    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0
        n = len(prices)
        once = [0]
        twice = [0]
        mini = prices[0]
        maxi = prices[-1]
        for i in range(1, n):
            p1 = prices[i]
            p2 = prices[-i]
            once.append(max(p1-mini, once[-1]))
            twice.append(max(maxi-p2, twice[-1]))
            mini = min(mini, p1)
            maxi = max(maxi, p2)
        return max([once[i]+twice[-i] for i in range(1, n)])
        
# 让我怀疑人生的大神解
class Spricelutipricen:
    def maxProfit(self, prices):
        a1,a2=-float('inf'),-float('inf')
        b1,b2=0,0
        for price in prices:
            # a1为历史最低价的负值
            if a1<-price:a1=-price
            # b1为历史最大盈利
            if b1<price+a1:b1=price+a1
            # a2 = b1 - 历史最大盈利后的最小值
            if a2<b1-price: a2=b1-price
            # b2为总和盈利
            if b2<a2+price:b2=a2+price
        return b2
# 个人理解
class Solution:
    def maxProfit(self, prices):
        mini = float('inf')
        his = 0
        miserly = -float('inf')
        earn = 0
        for price in prices:
            mini = min(price, mini)
            his = max(price-mini, his)
            miserly = max(his-price, miserly)
            earn = max(miserly+price, earn)
        return earn
