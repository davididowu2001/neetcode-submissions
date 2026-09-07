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
        def dfs(node):
            if not node:
                return
            clone = Node(node.val)
            hashy[node] = clone
            for n in node.neighbors:
                if n in hashy:
                    clone.neighbors.append(hashy[n])
                else:
                    # n hasnt been cloned yet, clone it
                    clone.neighbors.append(dfs(n))
            return clone
        return dfs(node)
