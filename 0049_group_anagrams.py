class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        
        mp={}
        for i in strs:
            sort="".join(sorted(i))
            print(sort)
            if sort in mp:
                mp[sort].append(i)
            else:
                mp[sort]=[i]

        return list(mp.values())
        
