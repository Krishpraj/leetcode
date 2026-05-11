class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        

    

        return [int(c) for c in list("".join([str(c) for c in nums]))]

        
 