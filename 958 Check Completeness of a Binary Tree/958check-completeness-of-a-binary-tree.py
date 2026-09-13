from collections import deque 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        

        
        qu=deque([(root,1)])
        ans=[]

        while qu: 
            curr=qu.popleft()
            print(curr[0].val)
            if ans and curr[1]!=ans[-1]+1:
                return False
            ans.append(curr[1])
            if curr[0].left:
                qu.append((curr[0].left,curr[1]*2))
            if curr[0].right:
                qu.append((curr[0].right,curr[1]*2+1))
            
        return True 


        



        