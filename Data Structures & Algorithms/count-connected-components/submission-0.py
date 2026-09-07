class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        graph = {i: [] for i in range(n)}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        count = 0
        def dfs(node):
            if node not in visited:
                visited.add(node)
                for n in graph[node]:
                    dfs(n)
        for node in range(n):
            if node not in visited:
                count += 1
                dfs(node)
        return count
'''
Algorithm

make an adjecency list of nodes and their neighbours
visited = set
count = 0
the dfs(node):
    if node not in visited:
        visitor.add (node)
        then traverse its neighbours

navigate node in range (n):
counter +=1
dfs(node)
return count

'''