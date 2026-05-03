class Solution:
    def rotatedDigits(self, n: int) -> int:
        
        count=0

        valid={2,5,6,9}
        invalid={0,1,8}

        def isvalid(x):
            x=str(x)
            status=False 
            for i in x:
                if (int(i) not in valid) and (int(i) not in invalid):
                    return False
                elif int(i) in valid:
                    status=True
            if status==False:
                return False 
            else:
                return True  
        
        for i in range(1,n+1):
            if isvalid(i):
                count+=1
            
        return count 