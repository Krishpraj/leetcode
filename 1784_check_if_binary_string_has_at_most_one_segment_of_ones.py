class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        brk=False
        for i in range(1,len(s)):
            if s[i]=="0":
                brk=True 
            if brk and s[i]=="1":
                return False
        return True 
        
