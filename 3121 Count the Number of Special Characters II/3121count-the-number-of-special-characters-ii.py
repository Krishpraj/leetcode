class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        
        lower={}
        higher={}

        for i,v in enumerate(word):
            if v.islower(): 
                    lower[v]=i
            else:
                if v.lower() in higher:
                    pass 
                else:
                    higher[v.lower()]=i
        
        count=0
        for i,v in lower.items():
            if i in higher and lower[i]<higher[i]:
                    count+=1
        
        return count 