# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        isValid = [True]
        def iterate(root, maximum, minimum):
            if not root:
                return
            if root.val >= maximum or root.val <= minimum:
                isValid[0] = False
                print(f"{root.val} broke it")
                return
            if root.left:
                iterate(root.left, min(maximum, root.val), min(minimum, root.val))
            if root.right:
                iterate(root.right, max(maximum, root.val), max(minimum, root.val))
            return
        iterate(root, float("inf"), float("-inf"))
        return isValid[0]