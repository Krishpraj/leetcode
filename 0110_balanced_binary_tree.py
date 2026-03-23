from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution: 
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        valid = True
        def dfs(node):
            nonlocal valid
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            if abs(left - right) > 1:
                valid = False
            
            return max(left, right) + 1
    
        dfs(root)
        return valid
    
    