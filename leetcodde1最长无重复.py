# 88.3%，本人解
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        s1, s3, max0 = set(), '', 0
        # if len(s) == 0:
        #     return 0
        max0 = 0
        for j in range(len(s)):
            if s[j] not in s1:
                s1.add(s[j])
                s3 += s[j]
            else:
                max0 = len(s3) if max0 < len(s3) else max0
                s3 = s3[s3.find(s[j])+1:] + s[j]
        return max(max0, len(s3))

s = Solution()
print(s.lengthOfLongestSubstring(''))

# 不回頭算法
'''最短
class Solution(object):
  def lengthOfLongestSubstring(self, s):
    prePos, last, ans = {}, -1, 0
    for idx, c in enumerate(s):
      last = max(prePos.get(c, -1), last)
      ans = max(ans, idx - last)
      prePos[c] = idx
    return ans
'''

'''最快
class Solution:
    def lengthOfLongestSubstring(self, s):

        """
        :type s: str
        :rtype: int
        """
        start = 0;
        end = 0;
        maxLen = 0
        sch = {}
        #print(sch)
        i = 0
        for ch in s:
            if ch in sch:
                if start <= sch[ch]:
                    start = sch[ch]+1;     
            sch[ch] = i            
            i +=1
            end = i
            if end-start > maxLen:
                maxLen = end-start
        return maxLen
'''
