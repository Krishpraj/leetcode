class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        
        pts=0
        multiplier=1
        for i,v in enumerate(s):
           if v=="(":
            multiplier*=2
           elif v==")":
            multiplier=multiplier//2
            if s[i-1]=="(":
                pts+=multiplier*1

        return pts  