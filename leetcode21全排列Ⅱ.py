class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums == []:
            return [[]]

        nums.sort()

        return self.permute(nums)

    def permute(self, nums):
        if len(nums) == 1 or nums[0] == nums[-1]:
            return [nums[0]]

        result = []

        for i, num in enumerate(nums):
            if nums[i] == nums[i-1]:
                continue
            stack = nums.copy()
            stack.pop(i)
            for addE in self.permute(stack):
                result.append([num]+addE)

        return result


s = Solution()
