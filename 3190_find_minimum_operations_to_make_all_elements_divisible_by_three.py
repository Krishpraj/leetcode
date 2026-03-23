class Solution:
    def minOperations(self, s: str) -> int:
        even=[]
        odd=[]
        for i in range(len(s)):
            if i%2!=0:
                odd.append(s[i])
            else:
                even.append(s[i])         
        return min(odd.count("0")+even.count("1"), odd.count("1")+even.count("0"))

