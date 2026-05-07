# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        

        def dfs(node,left,right):

            if node == None: 
                return True 

            if left is not None and node.val<=left:
                return False 

            if right is not None and node.val>=right:
                return False 

            left =  dfs(node.left,left,node.val)
            right = dfs(node.right,node.val,right)

            print(node.right,node.val,right)
            if left and right:
                return True
            
            return False
        
        return dfs(root, None, None )