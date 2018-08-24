class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        count = len(nums)-2
        if count == 1:
            return sum(nums)
        total = nums[0]+nums[1]+nums[2]
        minium = nums[0]+nums[1]+nums[2] - target
        for num in range(count):
            L = num + 1
            R = count + 1

            span = abs(nums[num] + nums[L] + nums[R] - target)

            if span < 0:
                L += 1
                continue
            elif span > 0:
                if minium > span or minium < 0:
                    minium = span
                    total = nums[num] + nums[L] + nums[R]
                R -= 1
            else:
                return nums[num] + nums[L] + nums[R]

        return total

'''
class Solution:
    
    def threeSumClosest(self, num, target):
        num.sort()
        result = num[0] + num[1] + num[2]
        for i in range(len(num) - 2):
            j, k = i + 1, len(num) - 1
            while j < k:
                sum = num[i] + num[j] + num[k]
                if sum == target:
                    return sum

                if abs(sum - target) < abs(result - target):
                    result = sum

                if sum < target:
                    j += 1
                elif sum > target:
                    k -= 1

        return result
'''
s = Solution()
print(s.threeSumClosest([1,1,1,0],-100))
