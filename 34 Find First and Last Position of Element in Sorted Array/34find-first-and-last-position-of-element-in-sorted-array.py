class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        
        

        def binarysearch(direction):
            l=0
            r=len(nums)-1
            idx=-1
            while l<=r:
                mid=(l+r)//2
                if nums[mid]==target:
                    idx=mid
                    if direction==1:
                        r=mid-1
                    if direction==0:
                        l=mid+1
                elif nums[mid]>target:
                    r=mid-1
                else:
                    l=mid+1
            
            return idx

        l=binarysearch(1)
        r=binarysearch(0)

        return [l,r]
    