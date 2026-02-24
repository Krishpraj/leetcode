# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:

        res=[]
        ans=[]
        def dfs(node):
            ans.append(str(node.val))
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            if not node.right and not node.left:
                res.append(ans[:])
            ans.pop()

        dfs(root)
        total=0

        for i in res:
            string="".join(i)
            total+=int(string,2)

        return total


    