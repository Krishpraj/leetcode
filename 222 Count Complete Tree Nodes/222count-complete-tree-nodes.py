# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode | None) -> int:
       

       def lefti(node):
            if not node:
                return 0
            else:
                return lefti(node.left)+1
        
       def righti(node):
            if not node:
                return 0
            else:
                return righti(node.right)+1


       def dfs(node):
            left=lefti(node)
            right=righti(node)
            if left==right:
                return 2**left-1
            else:
                return dfs(node.left)+dfs(node.right)+1
    
       return dfs(root)