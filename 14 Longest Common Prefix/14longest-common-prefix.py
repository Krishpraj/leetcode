class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        
        sample=strs[0]
        matched=[0]*len(strs)
        for i in range(len(strs)):
            for j in range(min(len(strs[i]),len(sample))):
                if strs[i][j]==sample[j]:
                    matched[i]+=1
                else:
                    break
                
        print(matched)
        return sample[0:min(matched)]      