# 使用排列组合知识，是在下弱鸡了
# 89.13%
class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        res = 1
        l = m + n - 1
        n = n if n < m else m
        # n = min(m, n)
        # 经测试，两者速率无差
        for i in range(l-n+1,l):
            res = res * i
        for j in range(1, n):
            res = res / j
        return int(res)
