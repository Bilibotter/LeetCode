class Solution:
    # 64.99%
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxium, rs, mstring, length = 0, ''.join(list(s[::-1])), '', len(s)

        if s == '':
            return ''

        for start, i in enumerate(s):
            end = rs.find(i)
            while end + start < length - 1:
                #if end == -1:
                #    break
                if end != 0:
                    palindrome = s[start:-end]
                else:
                    palindrome = s[start:]
                if len(palindrome) <= maxium:
                    break
                if palindrome == palindrome[::-1]:
                    maxium, mstring = len(palindrome), palindrome
                end = end + 1 + rs[end + 1:].find(i)

        if maxium == 0:
            return s[0]

        return mstring


class Solution:
    # @return a string
    def longestPalindrome(self, s):
        if len(s) == 0:
            return 0
        maxLen=1
        start=0
        for i in range(len(s)):
            if i-maxLen >= 1 and s[i-maxLen-1:i+1] == s[i-maxLen-1:i+1][::-1]:
                start = i-maxLen-1
                maxLen += 2
                continue

            if i-maxLen >= 0 and s[i-maxLen:i+1] == s[i-maxLen:i+1][::-1]:
                start = i-maxLen
                maxLen += 1

        return s[start:start+maxLen]


s = Solution()
print(s.longestPalindrome('abbabbbe'))