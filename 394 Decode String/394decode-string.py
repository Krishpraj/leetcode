class Solution:
    def decodeString(self, s: str) -> str:

        stk=[]
        arr=[]


        # 2[abc]3[cd]ef

        # 2
        # 2[
        # 2[ab
        # 2[abc
        # abcabc3[c
        # abcabc3[cd



        for i in s: 
            if i=="]":
                res=[]
                while stk[-1]!="[":
                    res.append(stk.pop())
                res=res[::-1]

                stk.pop() # pop "["

                times=""
                while stk and stk[-1].isnumeric():
                    times+=stk.pop()
                times=times[::-1]

                res=res*int(times)
                stk.extend(res)
            else:
                stk.append(i)
        
        return "".join(stk)