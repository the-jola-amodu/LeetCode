"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        if head == None:
            return None
        storage = dict()
        curr = head
        while curr:
            storage[curr] = Node(curr.val)
            curr = curr.next
        for old, new in storage.items():
            new.next = storage[old.next] if old.next else None
            new.random = storage[old.random] if old.random else None
        return storage[head]
        