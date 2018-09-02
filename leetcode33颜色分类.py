# 不知意义何在
class Solutions:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()


# 作死的写了一个特别慢的解
class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        counts = [0, 0, 0]
        while nums:
            counts[nums.pop()] += 1
        nums.extend([num for num, i in enumerate(count) for j in range(i)])


# 大神解法
class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # nums.sort()
        num0, num2 = 0, 0
        for i,n in enumerate(nums):
            if n == 0:
                num0 += 1
            if n == 2:
                num2 += 1
            nums[i] = 1
        if num0:
            nums[:num0] = [0] * num0
        if num2:
            nums[-num2:] = [2] * num2


s = Solution()
s.sortColors([2,0,2,1,1,0])

