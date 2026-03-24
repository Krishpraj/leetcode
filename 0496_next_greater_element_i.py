class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        

        ans=[]
        for i in range(len(nums1)):
            l=0
            found=False
            appended=False
            while l<len(nums2):
                if nums2[l]==nums1[i]:
                    found=True 
                elif nums2[l]>nums1[i] and found:
                    appended=True 
                    ans.append(nums2[l])
                    break
                l+=1

            if not appended:
                ans.append(-1)
        return ans



