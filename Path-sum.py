# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        
        if not root:
            return False  

        def dfs(node,sm):
            if not node.left and not node.right:
                if sm+node.val==targetSum:
                    return True
                return False

            x,y=False,False
            if node.left:
                x=dfs(node.left, sm+node.val) 
            if node.right:
                y=dfs(node.right, sm+node.val)
            return x or y 
        return dfs(root,0)  
