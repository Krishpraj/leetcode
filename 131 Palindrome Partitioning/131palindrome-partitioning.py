class Solution:
    def partition(self, s: str) -> List[List[str]]:
        

        # [a,a,b]
        #  [a]
        #
        #
        #
        res=[]
        ans=[]  
        mp={}
        def dfs(idx):
            if idx==len(s):
                res.append(ans[::])
                return 
            
            if idx in mp: 
                for i,v in mp[idx]:
                    ans.append(i)
                    dfs(v)
                    ans.pop()
                return 
        
            for i in range(idx,len(s)):
                if s[idx:i+1]==s[idx:i+1][::-1]:
                    ans.append(s[idx:i+1])
                    if idx not in mp:
                        mp[idx]=[]
                    mp[idx].append((s[idx:i+1],i+1))
                    dfs(i+1)
                    ans.pop()
        
        dfs(0)
        return res 
                
                
        

        