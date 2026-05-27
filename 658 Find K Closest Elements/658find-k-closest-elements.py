class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        idx=[float("inf"),0]
        for i in range(len(arr)): 
            dist=abs(arr[i]-x)
            if dist<idx[0]:
                idx[1]=i
                idx[0]=dist
        
        curr=idx[1]
        res=[]
        left=curr-1
        right=curr+1
        
        while len(res)!=k:
            print(left,right)
            res.append(arr[curr])
            dist1,dist2=float("inf"),float("inf")
            if right<len(arr):
                dist2=abs(arr[right]-x)
            if left>=0: 
                dist1=abs(arr[left]-x)
        
            if dist1<=dist2: 
                curr=left
                left-=1
            else: 
                curr=right
                right+=1
        
        return sorted(res)

