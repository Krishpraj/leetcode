class Solution:
    def getHappyString(self, n: int, k: int) -> str:


        res=[]
        ans=""
        def dfs():
            nonlocal ans
            if len(ans)==n:
                res.append(ans[:])
                return 
            
            if len(res)==k:
                return 
    
            for i in ['a','b','c']:
                if len(ans)>=1 and ans[-1]==i:
                    continue 
                else:
                    ans=ans+i
                    dfs()
                    ans=ans[:-1]
        
        dfs()
        print(res)
        if len(res)<=k-1:
            return ""
        else:
            return res[k-1]

