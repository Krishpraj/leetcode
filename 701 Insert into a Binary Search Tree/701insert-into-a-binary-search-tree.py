# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        
        if not root:
            return TreeNode(val)

        def dfs(node,prev,direction):
            if not node:
                if direction=="R":
                    prev.right=TreeNode(val)
                else:
                    prev.left=TreeNode(val)
                return 

            if val>node.val:
                dfs(node.right,node,"R")
            if val<node.val:
                dfs(node.left,node,"L")

        dfs(root,None,"")
        return root