# 超越98.94%
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        ll = len(nums1)+len(nums2)
        nums1.extend(nums2)
        nums1.sort()
        if ll % 2:
            return nums1[int(ll/2)]       
        else:
            return sum(nums1[int(ll/2)-1:int(ll/2)+1])/2
        
s = Solution()
print(s.findMedianSortedArrays([1,2], [3,4]))
