# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':


        found=None

        def dfs(node):

            nonlocal found 
            if not node:
                return 0

            count=0
            if node==p or node==q: 
                count+=1 

            count+=dfs(node.left)
            count+=dfs(node.right)

            if count==2 and not found: 
                found=node 

            return count 
            
        dfs(root)
        return found     
        