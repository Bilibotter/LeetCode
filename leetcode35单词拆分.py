# 逻辑优化版本
class Solution:
    # 81.3%
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        indexes = [True]+[False]*(len(s))
        wordList = [[]]*(len(s)+1)
        for word in wordDict:
            try:
                wordList[len(word)] = wordList[len(word)] + [word]
            except:
                continue
        for j in range(1, len(s)+1):
            for i, jud in enumerate(indexes[j::-1]):
                if jud:
                    if s[j-i:j] in wordList[i]:
                        indexes[j] = True
                        break
        print(indexes)
        return indexes[-1]
# 49.6%的慢
# class Solution:
#     # 嵌套列表坑的一批
#     def wordBreak(self, s, wordDict):
#         """
#         :type s: str
#         :type wordDict: List[str]
#         :rtype: bool
#         """
#         indexes = [True]+[False]*(len(s))
#         wordList = [[]]*(len(s)+1)
#         for word in wordDict:
#             try:
#                 wordList[len(word)] = wordList[len(word)] + [word]
#             except:
#                 continue
#         for j in range(1, len(s)+1):
#             for i, jud in enumerate(indexes[:j]):
#                 if jud:
#                     if s[i:j] in wordList[j-i]:
#                         indexes[j] = True
#                         break
#         return indexes[-1]


s = Solution()
s1 = "catsandog"
s2 = ["cats", "dog", "sand", "and", "cat"]
s.wordBreak(s1, s2)
