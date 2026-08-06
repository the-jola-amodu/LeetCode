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
            if curr in seen:
                return curr
            seen.append(curr)
            curr = curr.next

        return None
        