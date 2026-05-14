class Solution:
    def isGood(self, nums: List[int]) -> bool:
        
        if len(nums)==1:
            return False


        good=[c for c in range(1,len(nums))]
        good.append(good[-1])

        return sorted(nums)==good
