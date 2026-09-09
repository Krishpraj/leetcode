class Solution:
    def countCommas(self, n: int) -> int:

        # 0-999 0  10^0
        # 1000-999999  1  10^3 
        # 100 000-
        if n<=1:
            return 0 

        power=len(str(n))//3 if len(str(n))%3!=0 else len(str(n))//3-1
        
        power*=3

        count=0
        while power!=0:
            count+=(power//3)*(n-10**power+1)
            n=10**power-1
            power-=3

        return count 
            #number=number of commas * the next comma power 
            
