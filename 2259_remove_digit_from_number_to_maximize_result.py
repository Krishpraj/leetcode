class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        
        
        arr=list(number)
        ans=[]
        for i in range(len(arr)):
            test=list(number)
            if arr[i]==digit:
                test.pop(i)
                word="".join(test)
                ans.append(int(word))
        
        return str(max(ans))


        res="".join(arr)
        return res