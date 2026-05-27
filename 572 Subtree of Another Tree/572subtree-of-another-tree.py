# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # print all subtrees
        
        values=[]
        def dfs(node): 
            if not node:
                return
            if check(node,subRoot):
                return True
            return dfs(node.left) or dfs(node.right)
        
        def check(node1,node2):
            if not node1 and not node2:
                return True 
            if not node1 or not node2: 
                return False 
            if node1.val==node2.val:
                return check(node1.left,node2.left) and check(node1.right,node2.right)
            
        if dfs(root):
            return True 
        else:
            return False 