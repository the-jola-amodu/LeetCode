# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        max_path = [root.val]

        def dfs(root):
            if not root:
                return 0
            max_left = max(0, dfs(root.left))
            max_right = max(0, dfs(root.right))

            max_path[0] = max(max_path[0], (root.val + max_left + max_right))

            return root.val + max(max_left, max_right)

        dfs(root)
        return max_path[0]