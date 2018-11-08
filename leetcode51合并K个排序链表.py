# 学到神解，以后会写得更快更优雅
# 击败98.87
class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        vector = []
        for node in lists:
            while node:
                vector.append(node)
                node = node.next
        head = ListNode(0)
        cop =head
        for i in sorted(vector, key=lambda x:x.val):
            cop.next = i
            cop = cop.next
        return head.next
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
        
