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