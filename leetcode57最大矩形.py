class Solution:
    def maximalRectangle(self, matrix):
        if len(matrix) == 0:
            return 0
        ans = 0
        row = len(matrix)
        col = len(matrix[0])
        for i in range(row):
            before = 0
            for j in range(col):
                if matrix[i][j] == '0':
                    ele = 0
                else:
                    ele = before + 1
                matrix[i][j] = ele
                before = ele
        for i in range(row):
            for j in range(col):
                mini = matrix[i][j]
                if mini == 0:
                    continue
                span = 1
                for k in range(i+1, row):
                    if matrix[k][j] < mini:
                        break
                    span += 1
                for k in range(i-1, -1, -1):
                    if matrix[k][j] < mini:
                        break
                    span += 1
                ans = max(ans, span*mini)
        
        return ans
