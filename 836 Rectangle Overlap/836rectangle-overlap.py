class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        

        x1, y1, x2, y2 = rec1
        X1, Y1, X2, Y2 = rec2

        if X2 <= x1 or X1 >= x2:
            return False

        if Y2 <= y1 or Y1 >= y2:
            return False
        
        return True