class Solution:
    def averageOfLevels(self, root: TreeNode | None) -> list[float]:
        level = []
        if root is None:
            return []
        queue = deque([root])
        result = []

        while queue:
            level = []
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(sum(level)/len(level))
        return result
                