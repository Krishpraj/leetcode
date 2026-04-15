# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        stk=[]
        def preorder(node):
            if not node:
                return 
            
            stk.append(node)
            preorder(node.left)
            preorder(node.right)
        
        preorder(root)
        for i,v in enumerate(stk):
            if i+1==len(stk):
                v.right=None
            else:
                v.right=stk[i+1]
            v.left=None
