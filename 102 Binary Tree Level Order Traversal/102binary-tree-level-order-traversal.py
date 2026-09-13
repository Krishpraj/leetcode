# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        queue = deque([(root, 0)])
        levels = []
        depth = -1

        while queue:
            curr, cnt = queue.popleft()
            if cnt > depth:
                depth += 1
                levels.append([])

            levels[cnt].append(curr.val)

            if curr.left:
                queue.append((curr.left, cnt + 1))
            
            if curr.right:
                queue.append((curr.right, cnt + 1))


        return levels