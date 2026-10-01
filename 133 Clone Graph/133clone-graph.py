"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        adj={}
        visited=set()
        if not node:
            return 
     

        def dfs(node):
            if node.val in visited:
                return

            visited.add(node.val)

            # Make sure this node exists in the adjacency list
            if node.val not in adj:
                adj[node.val] = []

            for neighbor in node.neighbors:
                # Add the edge
                adj[node.val].append(neighbor.val)

                # DFS into the neighbor
                dfs(neighbor)

        dfs(node)
        print(adj)
        
        nodes=[]
        for i in range(1,len(adj.keys())+1):
            n=Node()
            n.val=i
            nodes.append(n)
        
        print([i.val for i  in nodes])
        
        for k,v in adj.items():
            nodes[k-1].neighbors=[nodes[i-1] for i in v]
        
        if nodes:
            return nodes[0]