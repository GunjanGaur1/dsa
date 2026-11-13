# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode | None, x: int, y: int) -> bool:
        if root is None:
            return []

        queue = deque([root])
        result = []
        parent = {}

        while queue:
            level = []
            n = len(queue)

            for i in range(n):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    parent[node.left.val] = node.val
                    queue.append(node.left)

                if node.right:
                    parent[node.right.val] = node.val
                    queue.append(node.right)
            if x in level and y in level:
                if parent[x]==parent[y]:
                    return False
                else:
                    return True

            print(parent)
        return False
