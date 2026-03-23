class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        nums=[list(i) for i in nums]
        ans=[]
        def dfs():
            if len(ans)==len(nums[0]) and ans not in nums:
                print(ans)
                return ans[:]
            elif len(ans)==len(nums[0]):
                return 
            else:
                ans.append("0")
                x=dfs()
                if x:
                    return x
                ans.pop()
                ans.append("1")
                y=dfs()
                if y:
                    return y
                ans.pop()
        
        x=dfs()
        y="".join(x)
        return y
