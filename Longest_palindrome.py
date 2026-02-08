class Solution:
    def longestPalindrome(self, s: str) -> str:

        maxlen=0
        res=""

        for i in range(len(s)):
            for j in range(i,len(s)):
                if j-i+1<=maxlen:
                    pass 
                elif s[i:j+1]==s[i:j+1][::-1] and (j-i+1>=maxlen):
                    maxlen=j-i+1
                    res=s[i:j+1]
        return res 
    


    