class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        res=[]

        l=0
        r=k

        while r<=len(nums):
            res.append(max(nums[l:r]))
            l+=1
            r+=1

        return res


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        heap = []
        output = []
        for i in range(len(nums)):
            heapq.heappush(heap, (-nums[i], i))
            if i >= k - 1:
                while heap[0][1] <= i - k:
                    heapq.heappop(heap)
                output.append(-heap[0][0])
        return output

        