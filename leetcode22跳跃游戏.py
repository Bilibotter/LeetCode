class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length = len(nums)
        can = [length-1]
        for i in range(length-2, -1, -1):
            if nums[i] + i >= can[-1]:
                can.append(i)
        return True if can[-1]==0 else False