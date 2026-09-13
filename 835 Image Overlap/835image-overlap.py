class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:

        
        def translate(dr,dc):
            count=0
            for i in range(len(img1)):
                for j in range(len(img1)):
                    if img1[i][j]==0:
                        continue

                    ni=i+dr
                    nj=j+dc

                    if 0<=ni<len(img1) and 0<=nj<len(img1):
                        if img2[ni][nj]==1:
                            count+=1
            
            return count


        a=0
        n=len(img1)
        for i in range(-n+1,n):
            for j in range(-n+1,n):
                a=max(a,translate(i,j))
        
        return a 