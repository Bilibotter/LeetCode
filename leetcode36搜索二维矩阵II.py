class Solution:
    def searchMatrix(self, matrix, target):
        """
        超越86.3%，常规操作
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        def searchMatrix(self, matrix, target):
            """
            :type matrix: List[List[int]]
            :type target: int
            :rtype: bool
            """
            if matrix == [[]]:
                return False
            for line in matrix[::-1]:
                if line[-1] >= target:
                    for i in line[::-1]:
                        if i == target:
                            return True
                        if i < target:
                            break
                else:
                    return False
            return False


# 让人费解的最快解，电脑测试仅超越16.4%
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for line in matrix:
            if target in line:
                return True
        return False
