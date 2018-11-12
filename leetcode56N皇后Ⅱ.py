class Solution:
    def totalNQueens(self, n):
        if n == 1:
            return n
        lst = []
        self.n = n
        self.res = 0
        self.total = {i for i in range(n)}
        for i in range(n):
            self.solve([i])
        return self.res

    def solve(self, lst):
        now = self.total - set(lst)
        for num in now:
            if self.conflict(lst, num):
                continue
            else:
                update = lst.copy()
                update.append(num)
                if len(update) == self.n:
                    self.res += 1
                else:
                    self.solve(update)

    def conflict(self, lst, i):
        kill = len(lst)
        for span, j in enumerate(lst):
            if abs(j - i) == kill - span:
                return True
        return False
