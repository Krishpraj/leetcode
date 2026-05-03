# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:


        res={}
        result=[]
        def dfs(node):
            nonlocal result
            if not node:
                return None

            l=dfs(node.right)
            r=dfs(node.left)

            if (l,node.val,r) in res:
                res[(l,node.val,r)]+=1
                if res[(l,node.val,r)]==2:
                    result.append(node)
            else:
                res[(l,node.val,r)]=1

            return (l,node.val,r)
            print(res)

        dfs(root)
        return result

             
            
    

