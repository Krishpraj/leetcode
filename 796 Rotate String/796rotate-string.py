class Solution:
    def rotateString(self, s: str, goal: str) -> bool:

        def shift():
            nonlocal s 
            string=s[1:len(s)]
            left=s[0]
            s=string+left

        for i in range(len(s)):
            shift()
            if s==goal:
                return True 
        
        return False 
            