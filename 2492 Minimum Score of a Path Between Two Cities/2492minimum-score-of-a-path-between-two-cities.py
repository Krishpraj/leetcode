class Solution:
    def minScore(self, n: int, roads: List[List[int]]):


        mp={}
        for i in range(len(roads)):
            if roads[i][0] in mp: 
                mp[roads[i][0]].append((roads[i][1],roads[i][2]))
            else: 
                mp[roads[i][0]]=[(roads[i][1],roads[i][2])]

            if roads[i][1] in mp: 
                mp[roads[i][1]].append((roads[i][0],roads[i][2]))
            else: 
                mp[roads[i][1]]=[(roads[i][0],roads[i][2])]
        
        print(mp)
        visited=set()
        ans=float('inf')
        def dfs(i):
            nonlocal ans
            visited.add(i)
            for j,k in mp[i]:
                ans=min(k,ans)
                if j not in visited:
                    dfs(j)
            return ans 
        
        return dfs(n)
            