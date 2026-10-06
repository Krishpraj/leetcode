class Solution:
    def trap(self, height: List[int]) -> int:
        
        trapped=0
        mn=0
        for i in range(len(height)):
            mx=max(height[i+1:len(height)],default=0)
            t=min(mn,mx)-height[i]
            if t>0:
                trapped+=t

            mn=max(mn,height[i])
        
        return trapped