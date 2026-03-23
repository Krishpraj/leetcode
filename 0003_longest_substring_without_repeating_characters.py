class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s=[c for c in s]
        mx=0
        ans=[]
        for i in range(len(s)):
            if s[i] in ans:
                while s[i] in ans:
                    ans.pop(0)
            ans.append(s[i])
            print(ans)
            mx=max(mx,len(ans))
        
        return mx 
    
    def alternative_solution(self, s: str) -> int:
        mp={}
        mx=0
        l=0
        for r in range(len(s)):
            if s[r] in mp and mp[s[r]]>=l:
                l=mp[s[r]]+1
            mp[s[r]]=r
            mx=max(mx,r-l+1)
        return mx