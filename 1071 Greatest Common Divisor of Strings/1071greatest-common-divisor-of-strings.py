class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

    
        starting=""
        if len(str2)<len(str1):
            starting=str2
        else:
            starting=str1
        
        while len(starting)>=1: 
            x=set(str1.split(starting))
            y=set(str2.split(starting))
             
            if len(x)==1 and len(y)==1 and x==y:
                return starting 
            starting=starting[:-1]
        
        return ""






