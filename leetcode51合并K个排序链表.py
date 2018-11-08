# 击败86.74%
class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        vector = []
        for node in lists:
            while node:
                vector.append(node.val)
                node = node.next
        ans = ListNode(0)
        head = ans
        for i in sorted(vector):
            ans.next = ListNode(i)
            ans = ans.next
        return head.next
        
