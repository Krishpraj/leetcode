class Solution:
    def maxDepth(self, s: str) -> int:
        

        mx=float('-inf')
        count=0
        for i in range(len(s)):
            if s[i]=="(":
                count+=1
            elif s[i]==")":
                count-=1    
            mx=max(mx,count)
        
        return mx 