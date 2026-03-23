
from pyparsing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:

        l=0
        r=len(height)-1
        ar=0
        while l<=r:
            area=(r-l)*min(height[r],height[l])
            ar=max(ar,area)

            if height[r]<height[l]:
                r-=1
            elif height[l]<height[r]:
                l+=1
            else:
                r-=1
                l+=1

        return ar    