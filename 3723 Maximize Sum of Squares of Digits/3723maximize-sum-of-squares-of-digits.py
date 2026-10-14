class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:

       max_digit=""
       total=0
       sm=sum
       if 9*num<sm:
            return max_digit

       while len(max_digit)<num and total<sm:
            for i in range(9,0,-1):
                if total+i<=sum:
                    total+=i
                    max_digit=max_digit+f"{i}"
                    break

       if len(max_digit)<num:
            max_digit=max_digit+"".join([str(0)]*(num-len(max_digit)))
        
       return max_digit
