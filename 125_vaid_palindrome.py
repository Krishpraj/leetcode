class Solution:
    def isPalindrome(self, s: str) -> bool:

        string=[]    
        for i in range(len(s)):
            if s[i].isalnum():
                string.append(s[i].lower())
        
        return string==string[::-1]
