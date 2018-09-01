# 有史以来最慢的一次，59.61%。
# 把except Exception改成except提高为84.38%
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        try:
            for num, line in enumerate(matrix):
                if line[0] > target:
                    break
            else:
                num += 1
            for i in matrix[num-1]:
                if i == target:
                    return True
            else:
                return False
                
        except:
            return False
