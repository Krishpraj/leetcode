class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:

       min_speed=1
       max_speed=max(piles)

       while min_speed<=max_speed:
            mid=(min_speed+max_speed)//2
            hours=0
            
            for i in range(len(piles)):
                hours+=math.ceil(piles[i]/mid)
            
        
    
            
            if hours<=h:
                max_speed=mid-1
            
            if hours>h:
                min_speed=mid+1

       return min_speed