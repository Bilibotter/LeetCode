# 仅超越60.20%
class Solution:
    def longestValidParentheses(self, s):
        """
        :type   s: str
        :rtype: int
        """
        if '()' not in s:
            return 0
        res = []
        count = 0
        status = 0
        dic = {'(': 1, ')': -1}
        for char in s:
            status += dic[char]
            count += 1
            if status == 0:
                res.append(count)
            elif status < 0:
                count = 0
                status = 0
            else:
                continue
        status = 0
        count = 0
        for char in s[::-1]:
            status -= dic[char]
            count += 1
            if status == 0:
                res.append(count)
            elif status < 0:
                count = 0
                status = 0
            else:
                continue
        return max(res)
# 大神写的最快解
class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [0]
        longest = 0

        for c in s:
            if c == "(":
                stack.append(0)
            else:
                if len(stack) > 1:
                    val = stack.pop()
                    stack[-1] += val + 2
                    longest = max(longest, stack[-1])
                else:
                    stack = [0]

        return longest


s = Solution()
print(s.longestValidParentheses("(()(((()"))
