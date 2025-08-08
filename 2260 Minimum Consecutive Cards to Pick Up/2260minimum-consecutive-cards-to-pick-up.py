class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:

        mapp = {}
        mini = float('inf')  # track minimum distance
        
        for i, v in enumerate(cards):
            if v in mapp:
                # calculate distance between current and last index of v
                length = i - mapp[v] + 1
                mini = min(length, mini)
            mapp[v] = i
        
        # if mini is unchanged, return -1 to indicate no duplicates found
        return mini if mini != float('inf') else -1

            
    


            
            
        