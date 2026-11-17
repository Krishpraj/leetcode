class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        
        nums1=set(nums1)
        nums2=set(nums2)

        res=[]
        for i in nums2:
            if i in nums1:
                res.append(i)

        return res 