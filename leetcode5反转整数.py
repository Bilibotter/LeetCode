class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = -1 if x < 0 else 1
        s = str(abs(x))[::-1]
        n = int(s) * flag
        return n if n.bit_length() < 32 else 0
