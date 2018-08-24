class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans = []

        while matrix:
            ans += matrix.pop(0)
            matrix = [*zip(*matrix)][::-1]

        return ans


s = Solution()
print(s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))