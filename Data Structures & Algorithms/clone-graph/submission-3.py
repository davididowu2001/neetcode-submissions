"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hashy = {}
        if not node:
            return
        def dfs(node):
           
            #main thing in the dfs is to clone to neighbour
            if node in hashy:
                return hashy[node] #return the clone if the node already exists
            
            clone = Node(node.val)
            hashy[node] = clone

            for n in node.neighbors:
               cloned_neighbor= dfs(n)
               clone.neighbors.append(cloned_neighbor)
            return clone
        return dfs(node)

