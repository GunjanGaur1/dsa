# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        if root is None:
            return False
        if root.val!=subRoot.val:
            left = self.isSubtree(root.left,subRoot)
            right = self.isSubtree(root.right,subRoot)
        
        else:
            if self.isSame(root, subRoot):
                return True
            else:
                left = self.isSubtree(root.left, subRoot)
                right = self.isSubtree(root.right, subRoot)
        return left or right


    def isSame(self, p, q):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        left = self.isSame(p.left, q.left)
        right = self.isSame(p.right, q.right)
        
        return left and right

