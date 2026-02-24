class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        s=[i for i in s]
        if k==1:
            if "0" in s and "1" in s:
                return True 

        def dfs():
            return 2**k
        x=dfs()
        res2=set()
        for i in range(len(s)-k+1):
            res2.add(tuple(s[i:i+k]))

        return len(res2)==x
            
    