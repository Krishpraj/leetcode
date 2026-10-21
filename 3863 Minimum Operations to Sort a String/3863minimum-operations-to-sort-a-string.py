class Solution:
    def minOperations(self, s: str) -> int:
     
       if list(s)==sorted(s):
            return 0 
       elif len(s)==2:
            return -1 
       elif s[0]==sorted(s)[0] or s[len(s)-1]==sorted(s)[len(s)-1]:
            return 1
       elif s[0]==sorted(s)[len(s)-1] and s[len(s)-1]==sorted(s)[0] and sorted(s)[len(s)-1]!=sorted(s)[len(s)-2] and sorted(s)[0]!=sorted(s)[1]:
            return 3
       else:
            return 2 
 