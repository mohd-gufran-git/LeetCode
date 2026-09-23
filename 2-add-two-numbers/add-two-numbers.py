# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:

            # l1 ka current value
            if l1:
                val1 = l1.val
            else:
                val1 = 0

            # l2 ka current value
            if l2:
                val2 = l2.val
            else:
                val2 = 0

            # Addition
            total = val1 + val2 + carry

            # Current digit
            digit = total % 10

            # Carry
            carry = total // 10

            # New node
            current.next = ListNode(digit)
            current = current.next

            # Next nodes
            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return dummy.next