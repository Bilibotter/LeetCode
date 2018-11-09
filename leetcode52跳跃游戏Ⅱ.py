# 超越96.4%
class Solution:
    def jump(self, nums):
        if len(nums) == 1:
            return 0
        ans = 1
        l = len(nums)-1
        i = 0
        now = 0 
        while i+nums[i] < l:
            maxi = 0
            num = nums[i]
            for j in range(1, num+1):
                k = i+j
                if nums[k]+j>maxi:
                    maxi = nums[k]+j
                    now = k
            i = now
            ans += 1
        return ans
