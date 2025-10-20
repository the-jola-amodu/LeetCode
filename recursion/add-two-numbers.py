# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = currSum = ListNode(0)
        extra = 0
        while l1 and l2:
            addition = l1.val + l2.val + carry
            carry = 0
            if addition > 9:
                carry += 1
                addition -= 10
            currSum.next = ListNode(addition)
            currSum = currSum.next
            l1 = l1.next
            l2 = l2.next
        if not l1 and l2:
            extra = l2
        if not l2 and l1:
            extra = l1
        while extra:
            addition = extra.val + carry
            carry = 0
            if addition > 9:
                carry += 1
                addition -= 10
            currSum.next = ListNode(addition)
            currSum = currSum.next
            extra = extra.next
        if carry != 0:
            currSum.next = ListNode(carry)
        return head.next


        
        