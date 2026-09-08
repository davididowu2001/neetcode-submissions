class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = {i:[] for i in range(n)}
        for a,b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
        
        visited = set()
        count = 0

        def dfs(node):
            if node  in visited:
                return
            visited.add(node)
            for neigh in adj_list[node]:
                if neigh in visited:
                    continue
                dfs(neigh)

        for i in range(n):
            if i not in visited:
                dfs(i)
                count +=1
        return count


'''
Algorithm

create an adjeceny list
{0: [1], 1:[0,2], 2:[1], 3:[4], 4:[3]}
and a visited set 
func dfs(node)
if node in visited:
    return
visited.add(node)
navigate through the node's neighbours calling dfs on them
increment count after one complete traversal


iterate through n:
    dfs(i)
    count += 1
return count

'''

