class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if target not in nums:
            return [-1, -1]
        from bisect import bisect_left, bisect_right
        return [bisect_left(nums, target), bisect_right(nums, target) - 1]
    