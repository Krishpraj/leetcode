class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        count=0

        def is_prime(n: int) -> bool:
            mp={2,3,5,7,11,13,17,19,23,29,31}
            if n in mp:
                return True
        

        for i in range(left,right+1):
            x=str(bin(i))
            y=x.count("1")
            if is_prime(y):
                count+=1
        return count

        