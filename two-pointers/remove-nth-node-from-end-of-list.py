# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        if head.next == None:
            return None
        dummy = ListNode()
        dummy.next = head
        herald = dummy
        for _ in range(n):
            herald = herald.next
        remover = dummy
        while herald and herald.next != None:
            herald = herald.next
            remover = remover.next
        remover.next = remover.next.next
        return dummy.next

        