class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        r = []
        l = []
        for i, row in enumerate(matrix):
            for j, ele in enumerate(row):
                if ele == 0:
                    if i not in r:
                        r.append(i)
                    if j not in l:
                        l.append(j)

        for i in r:
            for j in l:
                matrix[i][j] =\
                    ';0