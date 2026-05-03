class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:

        minimum = float('inf')
        mp = {}
        
        for i, v in enumerate(nums):
            if v in mp:
                minimum = min(minimum, i - mp[v])
            
            rev = int(str(v)[::-1])
            mp[rev] = i   # store reversed
        
        return -1 if minimum == float('inf') else minimum