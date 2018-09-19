class Solution:
    # 超越97.61%，庆祝一下
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        stack = [0]
        for i, line in enumerate(triangle):
            for j, ele in enumerate(line):
                if j == 0:
                    # print('start:', ele+stack[-i])
                    stack.append(ele+stack[-i])
                elif j == i:
                    # print('finish:', ele+stack[-i-1])
                    stack.append(ele+stack[-i-1])
                else:
                    # print('medium:', ele + min(stack[-i - 1], stack[-i]))
                    stack.append(ele+min(stack[-i-1], stack[-i]))
        print('stack:', stack)
        return min(stack[-i-1:])


s = Solution()
t = [[2],[3,4],[6,5,7],[4,1,8,3]]
s.minimumTotal(t)
