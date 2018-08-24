from math import factorial
class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        stack = [str(i+1) for i in range(n)]

        return self.Deal(n,k,stack,'')

    def Deal(self,n,remain,stack,state):
        if len(stack) == 1:
            return state + stack[0]
        mul = factorial(n-1)
        adv = remain / mul
        remain = remain % mul
        num = int(adv + bool(remain) - 1)
        state += stack.pop(num)

        return self.Deal(n-1,remain,stack,state)

