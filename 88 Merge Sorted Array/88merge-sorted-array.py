class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        l=0

        while l<(m+n-len(nums2)):
            print(l)
            if nums2 and nums2[0]<nums1[l]:
                curr=nums2.pop(0)
                for i in range(len(nums1)-1,l,-1):
                    nums1[i]=nums1[i-1]
                nums1[l]=curr 
            l+=1

        for i in range(m+n-len(nums2),len(nums1)):
            nums1[i]=nums2.pop(0)
        
        