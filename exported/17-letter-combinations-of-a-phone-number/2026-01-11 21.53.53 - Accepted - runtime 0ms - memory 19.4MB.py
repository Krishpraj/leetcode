class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dictionary={2:["a","b","c"],3:["d","e","f"],4:["g","h","i"],5:["j","k","l"]
        ,6:["m","n","o"],7:["p","q","r","s"],8:["t","u","v"],9:["w","x","y","z"]}
        
        digits=[int(i) for i in digits]
        print(digits)
        res=[]
        ans=""
        def backtrack(index):#1234 234 34 4
            nonlocal ans
            if len(ans)==len(digits) and ans not in res:
                res.append(ans)
                return 
            for i in dictionary[digits[index]]:
                temp=ans
                ans=ans+i
                backtrack(index+1)
                ans=temp

        backtrack(0)
        return res
            


        backtrack(0)


                
        

           