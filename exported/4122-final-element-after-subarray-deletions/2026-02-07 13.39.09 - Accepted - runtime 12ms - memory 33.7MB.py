class Solution:
    def finalElement(self, nums: List[int]) -> int:

        # if it alice turns she takes the minumum 2 
        # if it bobs turns she takes the maximum 
        # alice plays first

  
        alice = True

        while len(nums) > 1:
            k = len(nums) - 1

            # initial window
            window_sum = sum(nums[:k])
            best_sum = window_sum
            best_start = 0

            for i in range(k, len(nums)):
                window_sum += nums[i] - nums[i - k]

                if alice:
                    if window_sum < best_sum:
                        best_sum = window_sum
                        best_start = i - k + 1
                else:
                    if window_sum > best_sum:
                        best_sum = window_sum
                        best_start = i - k + 1

            # DELETE the chosen subarray
            nums = nums[:best_start] + nums[best_start + k:]
            alice = not alice

        return nums[0]
