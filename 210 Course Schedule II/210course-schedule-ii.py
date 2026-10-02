class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:

        mp={i:set() for i in range(numCourses)}
        for c,p in prerequisites:
            mp[c].add(p)
        graph={}
        for c,p in prerequisites:
            if p not in graph:
                graph[p]=set()
            graph[p].add(c)

        finished=[]
        q=collections.deque([i for i in mp if mp[i]==set()])
        while q:
            curr=q.popleft()
            finished.append(curr)
            if curr not in graph:
                continue 
            for i in graph[curr]:
                mp[i].remove(curr)
                if mp[i]==set():
                    q.append(i)
            
        
                
        if len(finished)==numCourses:
            return finished
        else:
            return []
                
        