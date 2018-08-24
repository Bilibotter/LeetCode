class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        dic = {}
        check = {'0': 0, '1': 0, '2': 0, '3': 1, '4': 1, '5': 1, '6': 2, '7': 2, '8': 2}
        for i in range(1, 10):
            dic[str(i)] = []

        for i in range(9):
            for j in range(9):
                newE = board[i][j]
                if newE == '.':
                    continue
                a0, b0 = i, j
                for a, b in dic[newE]:
                    if a0 == a or b0 == b:
                        return False
                    elif check[str(a0)] != check[str(a)] or check[str(b0)] != check[str(b)]:
                        continue
                    else:
                        return False
                dic[newE].append((i, j))

        return True


