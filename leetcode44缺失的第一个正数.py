# 超越90.9%
class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nnn = 1
        nums.sort()
        for num in nums:
            if num > nnn:
                break
            elif nnn == num:
                nnn += 1
        return nnn

# 依然超越90.91%
class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        n = 1
        while n in nums:
            n += 1
        return n
        
