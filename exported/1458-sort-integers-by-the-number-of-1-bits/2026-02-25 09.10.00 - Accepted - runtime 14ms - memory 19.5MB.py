class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        
        mp={}
        for i in arr:
            bits=[i for i in bin(i)]
            if bits.count("1") in mp:
                mp[bits.count("1")].append(i)
            else:
                mp[bits.count("1")]=[i]
        
        ans=[]
        for key in sorted(mp.keys()):
            ans.extend(sorted(mp[key]))
        
        return ans

