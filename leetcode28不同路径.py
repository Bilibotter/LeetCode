import math


# 数学解
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return math.factorial(m+n-2)/math.factorial(m-1)/math.factorial(n-1)


#相当于走了m+n-2步，其中m-1步向下走，n-1步向右走
#快速解法
class Solution:
    def uniquePaths(self, m, n):
        memo = [1 for _ in range(n)]
        for _ in range(1, m):
            for j in range(1, n):
                memo[j] += memo[j-1]
        return memo[n-1]