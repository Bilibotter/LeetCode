class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        end = len(nums) - 3
        if end == 1:
            return [nums] if sum(nums) - target == 0 else []
        r = end + 2
        stack = []
        for num in range(end):
            span = target - nums[num]
            # if nums[num] == nums[num+1] and num+1 <= end
            if nums[num] == nums[num+1]:
                continue
            for n in range(num + 1, r):
                L = n + 1
                R = r
                while L < R:
                    distance = nums[n] + nums[L] + nums[R] - span
                    if distance > 0:
                        R -= 1
                    elif not distance:
                        stack.append((nums[num], nums[n], nums[L], nums[R]))
                        L += 1
                    else:
                        L += 1

        return stack


s = Solution()
print(s.fourSum([1, 0, -1, 0, -2, 2], 0))
from sklearn.preprocessing import LabelEncoder