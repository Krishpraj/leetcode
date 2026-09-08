class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nm = sorted(nums)

        l = 0
        r = len(nm) - 1

        while l < r:
            if nm[l] + nm[r] == target:
                # Find the original indices
                left = nums.index(nm[l])
                
                # Find right index, making sure it's different from left
                right = nums.index(nm[r], left + 1) if nm[l] == nm[r] else nums.index(nm[r])
                
                return [left, right]

            elif nm[l] + nm[r] > target:
                r -= 1
            else:
                l += 1


