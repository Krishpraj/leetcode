class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        mp={}
        for i,v in enumerate(arr):
            if v in mp:
                mp[v]+=1
            else:
                mp[v]=1

        mp=dict(sorted(mp.items(), key=lambda item: item[1]))
        print(mp)

        while mp:
            i, val = next(iter(mp.items()))
            if k >= val:
                k -= val
                mp.pop(i)
            else:
                break

        return len(mp)