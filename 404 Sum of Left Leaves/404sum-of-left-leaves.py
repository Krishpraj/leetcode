# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        total=0

        def dfs(node,status):
            nonlocal total
            if not node.left and not node.right and status=="left":
                total+=node.val 
                return 
            
            if not node.left and not node.right:
                return 
            
            if node.left:
                dfs(node.left,"left")
            if node.right:
                dfs(node.right,"no")  

        dfs(root,"no")
        return total
