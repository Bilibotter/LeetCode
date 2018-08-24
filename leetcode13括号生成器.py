class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.result = []
        self.generateParenthesisIter('',n,n)
        return self.result

    def generateParenthesisIter(self, state, left, right):
        if not left:
            for i in range(right):
                state += ')'
            self.result.append(state)
            return
        self.generateParenthesisIter(state+'(', left-1, right)
        if left < right:
            self.generateParenthesisIter(state+')', left, right-1)


s = Solution()
print(s.generateParenthesis(3))