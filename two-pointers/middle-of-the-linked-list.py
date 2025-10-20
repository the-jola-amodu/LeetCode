# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        counter = 0
        curr = head
        while curr:
            counter += 1
            curr = curr.next
        middle = int(counter / 2)
        counter = 0
        curr = head
        while curr and counter < middle:
            counter += 1
            curr = curr.next
        return curr

        