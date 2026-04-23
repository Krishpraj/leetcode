class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        val=1

        for i in range(len(digits)-1,-1,-1):    
            if digits[i]+val>=10:
                digits[i]=0
            else:
                digits[i]+=val
                val=0
        
        if val==1:
            digits.insert(0,val)
        
        return digits
