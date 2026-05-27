class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size=len(s1)
        window=sorted(s1)

        for i in range(len(s2)-window_size+1):
            if sorted(s2[i:i+window_size])==window:
                return True
        
        return False 
            
        