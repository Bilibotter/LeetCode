class Solution:
    def __init__(self):
        self.maxium = []
    def transport(self, height):
        stack = []
        for num, h in enumerate(height):
            stack.append((num, h))

        return stack
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        height = self.transport(height)
        return self.maxarea(height)

    def maxarea(self, height):

        stack = []
        Length = len(height)
        H0 = height[0]
        H1 = height[-1]
        h0 = H0[1]
        h1 = H1[1]
        k = (h1-h0)/(H1[0]-H0[0]) if (H1[0]-H0[0]) else 0
        b = h0 - H0[0]*k
        if Length <= 2:
            k = min(h0, h1)*(H1[0]-H0[0])
            b = (H0[0], H1[0])
            for m in self.maxium:
                if m[2] > k:
                    k = m[2]
                    b = m[:2]
            return k

        for h in height[1:-1]:
            if h[1] < h[0] * k + b:

                continue
            else:
                stack.append(h)

        if h0 < h1:
            self.maxium.append((H0[0], H1[0], h0*(H1[0]-H0[0])))
            stack.append(height[-1])
            height.pop(0)
        else:
            self.maxium.append((H0[0], H1[0], h1*(H1[0]-H0[0])))
            stack.insert(0, height[0])
            height.pop()

        return self.maxarea(stack)

s = Solution()
List = [1, 3, 2, 5, 25, 24, 5]
print(s.maxArea(List))
