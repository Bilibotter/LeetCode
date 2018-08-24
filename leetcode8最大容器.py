class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        R = width = len(height)-1
        L = square = 0

        for w in range(width, 0, -1):
            if height[R] < height[L]:
                square = max(square, height[R]*w)
                R -= 1
            else:
                square = max(square, height[L]*w)
                L += 1

        return square


s = Solution()
List = [1, 3, 2, 5, 25, 24, 5]
print(s.maxArea(List))
