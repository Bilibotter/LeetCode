# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        ptr = dummyRoot = ListNode(0)

        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next

            if l2:
                carry += l2.val
                l2 = l2.next

            ptr.next = ListNode(carry % 10)
            ptr = ptr.next
            # faster than carry = int(carry/10)
            carry //=  10

        return dummyRoot.next


l1 = [1, 2, 3]
l2 = [4, 5, 6]

ptr = dummyRoot = ListNode(0)

for l in l1:
    ptr.next = l
    ptr = ptr.next

l1 = ptr.next

ptr = dummyRoot = ListNode(0)

for l in l2:
    ptr.next = l
    ptr = ptr.next

l2 = ptr.next

s = Solution()
s.addTwoNumbers(l1, l2)
