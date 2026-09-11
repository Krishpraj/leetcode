from collections import Counter
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:

        numbers=set()

        def dfs(num,arr):
            if len(num)==3:
                res="".join([str(c) for c in num])
                res=int(res)
                numbers.add(res)
                return 
            
            if len(num)==2:
                for i,v in enumerate(arr):
                    if v%2==0:
                        num.append(v)
                        dfs(num,arr[0:i]+arr[i+1:len(arr)])
                        num.pop()
                return 
            
            for i,v in enumerate(arr):
                if v==0 and len(num)==0:
                    continue 
                num.append(v)
                dfs(num,arr[0:i]+arr[i+1:len(arr)])
                num.pop()
        
        dfs([],digits)
        return len(numbers)