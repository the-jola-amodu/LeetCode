# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubPath(self, head, root):
        found = [False]

        def check(head, root):
            if head.val == root.val:
                if head.next:
                    if root.left:
                        check(head.next, root.left)
                    if root.right:
                        check(head.next, root.right)
                else:
                    found[0] = True
                    return
            return

        def traverse(head, root):
            if not root:
                return

            if head.val == root.val:
                check(head, root)
            else:
                if root.left:
                    traverse(head, root.left)
                if root.right:
                    traverse(head, root.right)
        traverse(head, root)
        return found[0]