class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        
        pre = []
        for i in range(len(nums)):
            curr = 0
            curr += nums[i]
            if pre:
                curr += pre[-1]
            
            pre.append(curr)
        
        sm = pre[-1] - x
        
        if sm < 0:
            return -1
        
        if sm == 0:
            return len(nums)
        
        l = 0
        r = 0

        mx = float('-inf')
        
        while r < len(nums):
            curr = pre[r] - (pre[l - 1] if l > 0 else 0)
            
            if curr < sm:
                r += 1
            elif curr == sm:
                mx = max(r - l + 1, mx)
                r += 1
            else:
                l += 1
                if l > r:
                    r = l

        if mx == float('-inf'):
            return -1
        
        return len(nums) - mx
