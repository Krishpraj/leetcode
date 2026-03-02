class Solution:
    def concatenatedBinary(self, n: int) -> int:
        final=""
        for i in range(1,n+1):
            final+=bin(i)[2:]

        return int(final,2)%(10**9+7)

        
