import math
import numpy as np
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            print(s)
            return
        numRows = int(numRows)
        row_len = math.ceil(len(s)/(numRows*2-2))*numRows
        A = np.full((numRows, row_len), ' ')
        turns = 0
        foot = numRows - 1

        for num, string in enumerate(s):
            judge = num % (numRows*2 - 2)

            if judge == 0 and num != 0:
                turns += 1
            if judge < numRows:
                A[judge][turns*foot] = string
            else:
                go = judge - numRows + 2
                A[-go][turns*foot+go-1] = string

        for row in A:
            print(''.join(row).strip())


s = Solution()
s.convert("PAYPALISHIRING", 3)
