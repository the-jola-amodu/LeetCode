# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        seen = []

        curr = head
        while curr:
            if curr.val in seen:
                return curr
            seen.append(curr.val)
            curr = curr.next

        return None
        