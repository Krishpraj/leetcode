class Solution:
    def reverse(self, x: int) -> int:
        neg=False
        if x<0:
            neg=True

        x=str(abs(x))
        x=x[::-1]
        x=int(x)
        if x<-2**31 or x>2**31-1:
            return 0 

        if neg==True:
            x=-x
        return x
    

    