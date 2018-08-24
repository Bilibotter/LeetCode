# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None:
            return None

        dummy = ListNode(0)
        dummy.next = head

        pre = dummy
        while head:
            if head.next:
                pre.next = head.next
                head.next.next, head.next = head, head.next.next
                pre, head = head, head.next
            else:
                head = None

        return dummy.next