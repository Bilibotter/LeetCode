# 仅超越74.84%...
# 想哭
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.stack = []
        num = self.maxSum(root)
        self.stack.append(num)
        return max(self.stack)

    def maxSum(self, root):
        s = []
        i = root.val
        if root.left:
            s.append(self.maxSum(root.left))
        if root.right:
            s.append(self.maxSum(root.right))
        s.append(i+sum(s))
        self.stack.append(max(s))
        s[-1] = 0
        return i + max(s)


s = Solution()
root = TreeNode(20)
root.left = TreeNode(15)
root.right = TreeNode(7)
root0 = TreeNode(9)
root1 = TreeNode(-10)
root1.left = TreeNode(9)
root1.right = root
s.maxPathSum(root1)
