class Solution:
    def countCommas(self, n: int) -> int:
       count=0
       for i in range(n+1):
            commas=len(str(i))//3
            if len(str(i))%3!=0:
                count+=commas
            else:
                count+=commas-1
       return count 