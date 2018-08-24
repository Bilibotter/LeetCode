class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}

        for string in strs:
            sortString = ''.join(sorted(string))
            if sortString in dic:
                dic[sortString].append(string)
            else:
                dic[sortString] = [string]

        return list(dic.values())
