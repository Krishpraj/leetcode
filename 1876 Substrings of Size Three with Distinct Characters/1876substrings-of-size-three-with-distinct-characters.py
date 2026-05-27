class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        
        queue=[]
        count=0
        for i in range(len(s)): 
            queue.append(s[i])
            if len(queue)>3:
                queue.pop(0)
            if len(queue)==len(set(queue))==3:
                count+=1
            print(len(queue),len(set(queue)))
        return count