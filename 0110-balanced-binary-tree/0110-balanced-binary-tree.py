# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        def height(root):
            if root is None:
                return 0

            left = height(root.left)
            right = height(root.right)

            if left==-1 or right==-1:
                return -1

            if abs(right-left)>1:
                return -1

            return 1 + max(left,right)

        height(root)

        return height(root)!=-1