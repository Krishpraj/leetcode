# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        ans=0
        res=""
        def dfs(node):
            nonlocal res,ans
            res+=str(node.val)
            print(res)

            if node.right:
                dfs(node.right)
            if node.left:
                dfs(node.left)
            if not node.left and not node.right:
                ans+=int(res)
            res=res[:-1]
        dfs(root)   
        return ans
        
