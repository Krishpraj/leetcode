class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def binarysearch():
            
            l=0
            r=len(matrix[0])*len(matrix)-1

            while l<=r:
                mid=(l+r)//2
                row, col = divmod(mid, len(matrix[0]))
                if matrix[row][col]==target:
                    return True 
                elif matrix[row][col]<target:
                    l=mid+1
                else:
                    r=mid-1

        if binarysearch():
            return True 
        else:
            return False

        