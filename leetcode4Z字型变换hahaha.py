class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        length = len(s)
        if numRows == 1 or numRows > length:
            return s
        List = ['']*numRows
        queue = numRows*2-2

        for num, word in enumerate(s):
            judge = num % queue
            if judge >= numRows:
                judge = abs(queue-judge)
            List[judge] += str(word)

        return ''.join(List)