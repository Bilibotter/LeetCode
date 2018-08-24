class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result = []

        for serno, num in enumerate(nums):
            Nums = nums.copy()
            state = Nums.pop(serno)
            self.recursive(Nums, [state])

        return self.result

    def recursive(self, nums, state):
        State = None
        if len(nums) <= 1:
            self.result.append(state+nums)
        else:
            for serno, num in enumerate(nums):
                Nums = nums.copy()
                State = Nums.pop(serno)
                self.recursive(Nums, state+[State])


s = Solution()
