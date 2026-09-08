class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = {i: [] for i in range(n)}
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
        
        visited = set()
        def dfs(parent, node):
            if node in visited and node!=parent:
                return False
            visited.add(node)
            for neighbour in adj_list[node]:
                if neighbour == parent:
                    continue
                if not dfs(node, neighbour): #issue is we see parent as negihbour and still add it to visited?  actually u cant add visited to a set. so does it just keep looping through first input and neighbour
                    return False
            return True
        if not dfs(-1, 0):
            return False
        return len(visited) == n


