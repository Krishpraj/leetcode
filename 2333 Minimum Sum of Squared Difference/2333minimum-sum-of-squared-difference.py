class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        
        
        d=[0]*100001
        tot=0
        mx=0
        for a,b in zip(nums1,nums2):
            diff=abs(a-b)
            d[diff]+=1
            mx=max(diff,mx)
            tot+=diff
        
        k=k1+k2

        if tot<=k:
            return 0
        
        
        for i in range(mx,0,-1):
            if k==0:
                break
            moves=min(k,d[i])
            d[i]-=moves
            d[i-1]+=moves
            k-=moves
        
        sm=0
        for i,v in enumerate(d):
            sm+=(i**2)*v
        
        return sm