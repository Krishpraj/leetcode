class Solution:
    def reverseBits(self, n: int) -> int:
        nums=[]
        for i in range(32):
            bit=n&1
            n=n>>1
            nums.append(bit)
        
        number=0
        for i in range(32):
            number+=nums[i]*((2)**(31-i))
        
        return number

        

    