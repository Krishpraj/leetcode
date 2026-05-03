class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mp={}
        for i in prerequisites:
            if i[0] in mp:
                mp[i[0]].append(i[1]) 
            else:
                mp[i[0]]=[i[1]]

        visiting=set()
        visited=set()
        def dfs(node):
            if node in visiting:
                return False  
            
            visiting.add(node)
            if node in mp: 
                for i in mp[node]:
                    if i in visited:
                        pass
                    elif not dfs(i):
                        return False
                    
            visiting.remove(node)
            visited.add(node)
            return True

      
        for i in mp.keys():
            if i in visited:
                pass 
            elif not dfs(i):
                 return False
        return True 
              
        
