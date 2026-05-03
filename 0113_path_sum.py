# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        res=[]
        path=[]
        if not root:
            return res
        def dfs(node):
            path.append(node.val)
            if not node.right and not node.left and sum(path)==targetSum:
                res.append(path[:])
            if node.right:
                dfs(node.right)
            if node.left:
                dfs(node.left)
            path.pop()

        dfs(root)
        return res
