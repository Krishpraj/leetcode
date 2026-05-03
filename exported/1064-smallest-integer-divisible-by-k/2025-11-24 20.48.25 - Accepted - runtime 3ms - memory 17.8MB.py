class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        
        # 1. Handle the non-solution case (Constraint)
        if k % 2 == 0 or k % 5 == 0:
            return -1
        
        # 2. Iterative Modular Reduction
        remainder = 0
        
        # The loop will run at most k times (Pigeonhole Principle)
        for length in range(1, k + 1):
            # Calculate the next repunit remainder R_L = (R_{L-1} * 10 + 1) mod k
            remainder = (remainder * 10 + 1) % k
            
            # Check for divisibility
            if remainder == 0:
                return length
        
        # This line should ideally never be reached due to the Pigeonhole Principle
        # and the constraint check, but it's good practice for safety.
        return -1
            