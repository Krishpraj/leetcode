# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        

        def dfs(rn,ln):
            if not rn and not ln:
                return True 
            if not rn or not ln:
                return False
            if rn.val!=ln.val:
                print(rn.val,ln.val)
                return False 

            return dfs(rn.left,ln.right) and dfs(rn.right,ln.left)            
        
            

        if not root.left and not root.right:
            return True
        elif root.left and root.right:
            return dfs(root.left,root.right)
        else:
            return False
