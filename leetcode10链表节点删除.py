# Definition for singly-linked list.
class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head.next is None:
            return None
        c = p = head
        for i in range(n):
            c = c.next
        if not c:
            return head.next
        while c.next:
            p = p.next
            c = c.next
        p.next = p.next.next
        return head

