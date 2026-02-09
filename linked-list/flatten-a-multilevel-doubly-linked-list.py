"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        stack = []
        curr = head
        while curr:
            if curr.child:
                if curr.next:
                    stack.append(curr.next)
                curr.next = curr.child
                curr.child.prev = curr
                curr.child = None
            curr = curr.next
        curr = head
        while curr.next:
            curr = curr.next
        while stack:
            node = stack.pop()
            curr.next = node
            curr.next.prev = curr
            while curr.next != None:
                curr = curr.next
        return head
        