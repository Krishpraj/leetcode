# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        inv=[]
        arr=[]
        
        def dfs(node):

            if not node:
                return 

            left=dfs(node.left)
            arr.append(node)
            right=dfs(node.right)

        dfs(root)
        for i,v in enumerate(arr):
            if i>0 and arr[i].val<arr[i-1].val:
                inv.append((arr[i-1],arr[i]))
        
        if len(inv)==1:
            inv[0][0].val,inv[0][1].val=inv[0][1].val,inv[0][0].val
        if len(inv)==2:
            inv[0][0].val,inv[1][1].val=inv[1][1].val,inv[0][0].val
        
