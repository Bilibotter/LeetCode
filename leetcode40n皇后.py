class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.n = n
        self.stack = []
        status = [1 for i in range(n)]
        line = ['.' for i in range(n)]
        self.solve(status, [])
        ret = []
        for ans in self.stack:
            res = []
            for i in ans:
                s = '.'*i + 'Q' + '.'*(n-i-1)
                res.append(s)
            ret.append(res)
        return ret

    def solve(self, status, history):
        def confict(past, now):
            inc = len(past)
            for num, q in enumerate(past):
                if abs(q-now) in (0, inc-num):
                    return True
            return False

        for num, i in enumerate(status):
            if i and not confict(history, num):
                s, h = status.copy(), history.copy()
                s[num] = 0, h.append(num)
                if len(h) == self.n:
                    self.stack.append(h)
                else:
                    self.solve(s, h)


s = Solution()
print(s.solveNQueens(4))
