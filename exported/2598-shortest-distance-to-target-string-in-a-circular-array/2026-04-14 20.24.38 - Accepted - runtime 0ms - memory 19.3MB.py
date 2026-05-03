class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:

        
        minlength=float('inf')
        for i in range(startIndex, len(words)+startIndex):
            if words[i%len(words)]==target:
                minlength=min(minlength,i-startIndex)

        for i in range(startIndex, -len(words)+startIndex,-1):
            if words[i%len(words)]==target:
                minlength=min(minlength,abs(i-startIndex))

        if minlength==float('inf'):
            return -1   
        return minlength