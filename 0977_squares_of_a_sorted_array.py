
from pyparsing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        nums=sorted([c**2 for c in nums])
        return nums
        