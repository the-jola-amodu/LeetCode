# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        if root == None:
            return max_depth
        else:
            max_depth = 1
        return max(max_depth + self.maxDepth(root.left), max_depth + self.maxDepth(root.right))
        