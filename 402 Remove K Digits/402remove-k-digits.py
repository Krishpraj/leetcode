class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        

        # 453
        nums=[int(c) for c in num]
        stack=[]
        curr=0
        for i in range(len(nums)):
            while k and stack and nums[i]<stack[-1]:
                stack.pop()
                k-=1
            stack.append(nums[i])
            
        while k:
            stack.pop()
            k-=1

        string="".join([str(c) for c in stack])
        string=string.lstrip("0")

        if string=="":
            return "0"
        else:
            return string 
