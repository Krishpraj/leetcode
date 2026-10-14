# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        q=[(root,1)]
        if not root:
            return 0 

        while q:
            nd=q.pop(0)
            curr=nd[0]
            level=nd[1]
            
            if not curr.left and not curr.right:
                return level 
            if curr.left:
                q.append((curr.left,level+1))
            if curr.right:
                q.append((curr.right,level+1))

