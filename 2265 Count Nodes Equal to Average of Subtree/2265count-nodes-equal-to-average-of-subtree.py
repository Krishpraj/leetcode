
from collections import Counter
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        

        ans=0

        def dfs(node):
            nonlocal ans

            

            if not node.left and not node.right:
                ans+=1
                return (node.val,1) #sum,count
            
            sm, count=node.val,1
            if node.left:
                res=dfs(node.left)
                sm+=res[0]
                count+=res[1]
                
            if node.right:
                res=dfs(node.right)
                sm+=res[0]
                count+=res[1] 
        
            avg=sm//count
            if node.val==avg:
                ans+=1

            return (sm,count)

        dfs(root)
        return ans
    
    