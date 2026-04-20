class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        
        maximum_distance=0
        for i in range(len(colors)):
            for j in range(len(colors)-1,i-1,-1):
                if colors[j]!=colors[i]:
                    maximum_distance=max(maximum_distance,j-i)
                    break
        
        return maximum_distance