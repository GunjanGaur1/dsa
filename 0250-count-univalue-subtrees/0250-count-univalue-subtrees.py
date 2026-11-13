# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: TreeNode | None) -> int:
        count = 0
        def dfs(root):
            nonlocal count
            if root is None:
                return True

            left = dfs(root.left)
            right = dfs(root.right)
            if not left or not right:
                return False

            if root.left and root.left.val!=root.val:
                return False
            if root.right and root.right.val!=root.val:
                return False

            count = count + 1
            return True

        dfs(root)
        return count

            
