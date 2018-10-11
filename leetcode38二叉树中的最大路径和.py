# 解决曾弃用解的逻辑漏洞，超越87.12%
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
        i = root.val
        r = self.maxSum(root.right) if root.right else -float('inf')
        l = self.maxSum(root.left) if root.left else - float('inf')
        self.stack.append(max(l+r+i, l, r))
        return i+max(r, l, 0)


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
        i = root.val
        r = root.right if root.right else -float('inf')
        l = root.left if root.left else - float('inf')
        if r > 0:
            self.stack.append(max(l+r+i, l, r))
        return i+max(r, l, 0)


s = Solution()
root = TreeNode(20)
root.left = TreeNode(15)
root.right = TreeNode(7)
root0 = TreeNode(9)
root1 = TreeNode(-10)
root1.left = TreeNode(9)
root1.right = root
s.maxPathSum(root1)
