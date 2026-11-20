# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        
        if not root: 
            return 0 
        
        mx=-1

        def dfs(node):
            nonlocal mx 
            if not node:
                return 0 

            left=dfs(node.left)
            right=dfs(node.right)

            mx=max(left+right,mx)
            return max(left,right)+1 
        
        dfs(root)
        return mx 