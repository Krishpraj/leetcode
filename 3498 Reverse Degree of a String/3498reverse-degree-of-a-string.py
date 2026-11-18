class Solution:
    def reverseDegree(self, s: str) -> int:
        alp="abcdefghijklmnopqrstuvwxyz"
        alp=alp[::-1]

        tot=0
        for i in range(len(s)):
            tot+=(alp.index(s[i])+1)*(i+1)
        return tot