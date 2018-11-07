class Solution():
    def trap(self, height):
        if not height:
            return 0
        rain = 0
        maxLeft = 0
        vector = []
        for h in height:
            maxLeft = max(h, maxLeft)
            vector.append(maxLeft)
        maxRight = 0
        for i in range(len(vector)-1, -1, -1):
            h = height[i]
            m = vector[i]
            maxRight = max(h, maxRight)
            dec = min(m, maxRight) - h
            if dec > 0:
                rain += dec
        return rain
