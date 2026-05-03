# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:

        mp={}

        if not root :
            return []

        def dfs(node, level):
            if level in mp:
                mp[level].append(node.val)
            else:
                mp[level]=[node.val]
            
            if node.right:
                dfs(node.right,level+1)
            if node.left:
                dfs(node.left,level+1)
        
        dfs(root, 0)
        li=[]

        for i in mp.values():
            li.append(max(i))
        return li