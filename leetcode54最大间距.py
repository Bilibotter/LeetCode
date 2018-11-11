# 击败100%
class Solution:
    def maximumGap(self, nums):
        if len(nums) <= 1:
            return 0
        nums.sort()
        maxi = 0
        before = nums[0]
        for num in nums[1:]:
            if num - before > maxi:
                maxi = num - before
            before = num
        return maxi
